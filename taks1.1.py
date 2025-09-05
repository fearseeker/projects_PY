from bs4 import BeautifulSoup
import requests

url = 'https://webscraper.io/test-sites/e-commerce/static/computers/laptops'
response = requests.get(url)
print("Статус:", response.status_code)
soup = BeautifulSoup(response.text, "html.parser")
laptops = []

items = soup.find_all("div", class_="thumbnail")

for item in items:
    price_elem = item.find("h4", class_="price")
    price = price_elem.text.strip()

    name_elem = item.find("a", class_="title")
    name = name_elem.text.strip()

    description_elem = item.find("p", class_="description")
    description = description_elem.text.strip()

    reviews_elem = item.find("p", class_="pull-right")
    reviews = reviews_elem.text.strip() if reviews_elem else "0 reviews"

    rating = len(item.find_all("span", class_="glyphicon-star"))

    laptops.append({
        "Ціна": price,
        "Назва": name,
        "Опис": description,
        "Відгуки": reviews,
        "Рейтинг": rating
        })

for laptop in laptops:
    print(f"Назва: {laptop['Назва']}")
    print(f"Ціна: {laptop['Ціна']}")
    print(f"Опис: {laptop['Опис']}")
    print(f"Відгуки: {laptop['Відгуки']}")
    print(f"Рейтинг: {laptop['Рейтинг']}")
    print("-" * 50)