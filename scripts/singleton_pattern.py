class SingletonExample:
    _instance = None

    def __new__(cls):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            print("Instance created with id:", id(cls._instance))
        return cls._instance

class SingletonPattern:
    @staticmethod
    def main():
        a = SingletonExample()
        b = SingletonExample()
        print("ID of a:", id(a))
        print("ID of b:", id(b))
