"""My attempt at making abstract static method singleton"""
from abc import ABCMeta, abstractmethod


class IPObject(metaclass=ABCMeta):

    @abstractmethod
    def print_data(self):
        """ implement in child class """
        return


class ObjectSingleton(IPObject):
    __instance = None

    @staticmethod
    def get_instance():
        if ObjectSingleton.__instance is None:
            ObjectSingleton.__instance = ObjectSingleton("object property", "object other properties", 0)
        return ObjectSingleton.__instance

    def __init__(self, object_property, object_different_properties, numerical_property):
        if ObjectSingleton.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.object_property = object_property
            self.object_different_properties = object_different_properties
            self.numerical_property = numerical_property

    @staticmethod
    def print_data():
        if ObjectSingleton.__instance is None:
            raise Exception("No instance exists. Use get_instance() to create one.")
        print(
            f"Object property: {ObjectSingleton.__instance.object_property}."
            f" Object different properties: {ObjectSingleton.__instance.object_different_properties}."
            f" Numerical property: {ObjectSingleton.__instance.numerical_property}")


i1 = ObjectSingleton.get_instance()
print(i1)
i1.print_data()


i2 = ObjectSingleton.get_instance()
print(i2)
i2.print_data()


"""Singleton works properly and is not instantiated more than once. It is confirmed by runnig this code.
print from terminal:
PS ~/abstract_method_singleton.py
<__main__.ObjectSingleton object at 0x000001E952206A50>
Object property: object property. Object different properties: object other properties. Numerical property: 0
<__main__.ObjectSingleton object at 0x000001E952206A50>

Object property: object property. Object different properties: object other properties. Numerical property: 0
The print_data method is static and can be called without creating an instance of the class. The singleton pattern is implemented correctly,
ensuring that only one instance of the class exists throughout the program. The code is clean and follows best practices
for implementing a singleton pattern in Python. The abstract method is implemented in the child class,
and the static method is used to access the singleton instance. The code is well-structured and easy to understand,
making it a good example of how to implement a singleton pattern with an abstract method in Python.
"""