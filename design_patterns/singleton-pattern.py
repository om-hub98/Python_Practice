class SingletonExample:
    instance = None
    a=10

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            print("Creating object...")
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, a:int):
        print("Initializing...")
        self.a = a

obj1 = SingletonExample(100)
obj2 = SingletonExample(200)

print(obj1 is obj2)

obj3 = SingletonExample(300)
print(obj1.a)