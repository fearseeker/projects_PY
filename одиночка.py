class Single:
    #проверяю есть ли уже объект
    instance = None

    def __new__(cls):
        if Single.instance is None:
            Single.instance = super().__new__(cls)
        return Single.instance
S1 = Single()
S2 = Single()
print(S1 is S2)
