class SingleMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class A(metaclass=SingleMeta):
    def __init__(self, a):
        self.a = a


a1 = A(2)
a2 = A(5)
print(a1.a, a2.a)
a2.a = 5
print(a1 is a2)
print(a1.a, a2.a)
