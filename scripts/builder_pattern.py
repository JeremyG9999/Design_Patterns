from abc import ABC, abstractmethod

class Product:
    def __init__(self):
        self.rice = None
        self.meat = None

    def __str__(self):
        return f"Bowl with {self.rice} rice and {self.meat} meat."

class Builder(ABC):  # Abstract Builder
    @abstractmethod
    def set_rice(self, rice):
        pass

    @abstractmethod
    def set_meat(self, meat):
        pass

    @abstractmethod
    def get_result(self):
        pass

class Concrete_Builder(Builder):  # Concrete Builder
    def __init__(self):
        self.product = Product()

    def set_rice(self, rice):
        self.product.rice = rice

    def set_meat(self, meat):
        self.product.meat = meat

    def get_result(self):
        return self.product

class Director:  # Director
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.set_rice("white")
        self.builder.set_meat("chicken")
        return self.builder.get_result()

class BuilderPattern:
    @staticmethod
    def main():
        director = Director(Concrete_Builder())
        print(director.construct())
