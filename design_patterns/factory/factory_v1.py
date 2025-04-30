from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def get_property(self):
        pass


class ProductA(Product):
    def get_property(self):
        return "Property of Product A"


class ProductB(Product):
    def get_property(self):
        return "Property of Product B"


class ProductFactory(ABC):
    @abstractmethod
    def create(self) -> Product:
        pass


class ProductAFactory(ProductFactory):
    def create(self) -> Product:
        return ProductA()
    

class ProductBFactory(ProductFactory):
    def create(self) -> Product:
        return ProductB()
    

def client_code(factory: ProductFactory):
    product = factory.create()
    print(product.get_property())


client_code(ProductAFactory())
client_code(ProductBFactory())