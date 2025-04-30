from abc import ABCMeta, abstractmethod


class IPObject(metaclass=ABCMeta):

    @abstractmethod
    def print_data(self):
        """ implement in child class """
        return


class ObjectSingleton(IPObject):

    __instance = None

    @staticmethod
    def get_instance(object_property="default property", object_different_properties="default other properties", numerical_property=0):
        if ObjectSingleton.__instance is None:
            ObjectSingleton.__instance = ObjectSingleton(object_property, object_different_properties, numerical_property)
        return ObjectSingleton.__instance
    
    def __init__(self, object_property, object_different_property, numerical_property):
        if ObjectSingleton.__instance is not None:
            raise Exception("Singleton cannot be instantiated more than once!")
        else:
            self.object_property = object_property
            self.object_different_property = object_different_property
            self.numerical_property = numerical_property

    @staticmethod
    def print_data():
        if ObjectSingleton.__instance is None:
            raise Exception("No instance exists. Use get_instance() to create one.")
        print(
            f"Object property: {ObjectSingleton.__instance.object_property}."
            f" Object different properties: {ObjectSingleton.__instance.object_different_property}."
            f" Numerical property: {ObjectSingleton.__instance.numerical_property}")
        

i1 = ObjectSingleton.get_instance("Custom property", "Other Custom property", 42)
print(i1)
i1.print_data()

i2 = ObjectSingleton.get_instance("Custom property 2", "Other Custom property 2", 42 + 2)
print(i2)
i2.print_data()
        