from __future__ import annotations
from abc import ABC, abstractmethod

class Creator(ABC):
    
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = product.operation()
        return f"Result of operation: {result}"


class ConcreteCreator1(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct1()

class ConcreteCreator2(Creator):

    def factory_method(self) -> Product:
        return ConcreteProduct2()

class Product(ABC):

    @abstractmethod
    def operation(self) -> str:
        pass

class ConcreteProduct1(Product):

    def operation(self) -> str:
        return self.__class__.__name__

class ConcreteProduct2(Product):

    def operation(self) -> str:
        return self.__class__.__name__


# Client Code
product = ConcreteCreator1()
print(product.some_operation())

product = ConcreteCreator2()
print(product.some_operation())