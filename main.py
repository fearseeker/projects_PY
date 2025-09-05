# app.py
import asyncio
from typing import List, Optional

import httpx
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from tortoise import fields, Tortoise
from tortoise.models import Model
from tortoise.contrib.fastapi import register_tortoise

GOREST_BASE = "https://gorest.co.in/public/v2"


# ---------- DB MODELS ----------
class User(Model):
    id = fields.IntField(pk=True)  # Використаємо той самий id, що й у GoREST
    name = fields.CharField(max_length=255, null=False)
    email = fields.CharField(max_length=255, null=True, unique=True)
    gender = fields.CharField(max_length=50, null=True)
    status = fields.CharField(max_length=50, null=True)

    posts: fields.ReverseRelation["Post"]


class Post(Model):
    id = fields.IntField(pk=True)  # Використаємо той самий id, що й у GoREST
    user: fields.ForeignKeyRelation[User] = fields.ForeignKeyField(
        "models.User", related_name="posts", on_delete=fields.CASCADE
    )
    title = fields.CharField(max_length=500, null=False)
    body = fields.TextField(null=True)


# ---------- SCHEMAS ----------
class PostOut(BaseModel):
    id: int
    user_id: int
    title: str
    body: Optional[str] = None

    class Config:
        from_attributes = True


class UserOut(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    gender: Optional[str] = None
    status: Optional[str] = None

    class Config:
        from_attributes = True


class UserWithPostsOut(UserOut):
    posts: List[PostOut] = []


# ---------- APP ----------
app = FastAPI(title="GoREST mirror API", version="1.0.0")


# ---------- INITIAL DATA LOADER ----------
async def fetch_all_pages(client: httpx.AsyncClient, url: str, params: Optional[dict] = None):
    """
    Витягує всі сторінки з GoREST (пагінація через заголовок Link).
    """
    results = []
    page = 1
    while True:
        p = {"page": page, "per_page": 100}
        if params:
            p.update(params)
        r = await client.get(url, params=p, timeout=30.0)
        r.raise_for_status()
        data = r.json()
        if not data:
            break
        results.extend(data)
        # Перевіряємо, чи є ще сторінки (проста евристика)
        link = r.headers.get("Link", "")
        if 'rel="next"' not in link:
            break
        page += 1
    return results


async def load_initial_data_if_empty():
    """
    Якщо БД порожня — завантажує користувачів і їх пости з GoREST і зберігає в SQLite.
    """
    # Чи є хоч один користувач?
    existing = await User.all().limit(1)
    if existing:
        return

    async with httpx.AsyncClient(base_url=GOREST_BASE, headers={"User-Agent": "fastapi-tortoise-httpx"}) as client:
        # Користувачі
        users = await fetch_all_pages(client, "/users")
        if not users:
            return

        # Збереження користувачів
        user_objs = []
        for u in users:
            user_objs.append(
                User(
                    id=u.get("id"),
                    name=u.get("name"),
                    email=u.get("email"),
                    gender=u.get("gender"),
                    status=u.get("status"),
                )
            )
        await User.bulk_create(user_objs, ignore_conflicts=True)

        # Для ефективності — тягнемо пости частинами паралельно
        async def fetch_posts_for_user(user_id: int):
            try:
                posts = await fetch_all_pages(client, "/posts", params={"user_id": user_id})
                return user_id, posts
            except Exception:
                return user_id, []

        tasks = [fetch_posts_for_user(u.get("id")) for u in users]
        results = await asyncio.gather(*tasks)

        post_objs = []
        for user_id, posts in results:
            for p in posts:
                post_objs.append(
                    Post(
                        id=p.get("id"),
                        user_id=user_id,
                        title=p.get("title") or "",
                        body=p.get("body"),
                    )
                )
        if post_objs:
            await Post.bulk_create(post_objs, ignore_conflicts=True)


# ---------- ROUTES ----------
@app.on_event("startup")
async def on_startup():
    # Ініціалізувати ORM
    await Tortoise.init(
        db_url="sqlite://gorest.sqlite3",
        modules={"models": ["__main__"]},
    )
    await Tortoise.generate_schemas()
    # Завантажити дані, якщо порожньо
    await load_initial_data_if_empty()


@app.on_event("shutdown")
async def on_shutdown():
    await Tortoise.close_connections()


@app.get("/users", response_model=List[UserOut], summary="Отримати всіх користувачів")
async def get_users():
    users = await User.all().order_by("id")
    return [UserOut.model_validate(u) for u in users]


@app.get("/users/{user_id}", response_model=UserOut, summary="Отримати користувача за ID")
async def get_user(user_id: int):
    user = await User.filter(id=user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return UserOut.model_validate(user)


@app.get(
    "/users/{user_id}/posts",
    response_model=List[PostOut],
    summary="Отримати всі пости користувача за ID"
)
async def get_user_posts(user_id: int):
    # Переконаємось, що користувач існує (опційно, щоб 404 був чітким)
    exists = await User.filter(id=user_id).exists()
    if not exists:
        raise HTTPException(status_code=404, detail="User not found")
    posts = await Post.filter(user_id=user_id).order_by("id")
    return [PostOut.model_validate(p) for p in posts]


# ---------- TORTOISE/FASTAPI INTEGRATION (опц.) ----------
# Це додасть /docs/swagger та /redoc інтегровано та healthcheck
register_tortoise(
    app,
    db_url="sqlite://gorest.sqlite3",
    modules={"models": ["__main__"]},
    generate_schemas=False,  # ми вже робимо це в on_startup
    add_exception_handlers=True,
)