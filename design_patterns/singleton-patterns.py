class Singleton:

    _instance = None
    _initialized = False

    def __new__(cls):
        """
        This methods is used for creating a new instance of the class.
        """
        if cls._instance is None:
            print("Creating object...")
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
            """
            It's a constructor in Python.
            This method is used for initializing the instance of the class.
            """
            if not self._initialized:
                 print("Initializing object...")
                 self._initialized = True
            else:
                print("Already initialized object...")
    

obj1 = Singleton()
print(f"obj1 initilization is done: {obj1._initialized}")
obj2 = Singleton()
print(f"obj2 initilization is done: {obj2._initialized}")
print(f"obj1 is obj2: {obj1 is obj2}")