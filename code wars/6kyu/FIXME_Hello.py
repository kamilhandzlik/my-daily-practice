"""
The code provided has a method hello which is supposed to show only those attributes which have been explicitly set. Furthermore, it is supposed to say them in the same order they were set.

But it's not working properly.

Notes
There are 3 attributes

name
age
sex ('M' or 'F')
When the same attribute is assigned multiple times the hello method shows it only once. If this happens the order depends on the first assignment of that attribute, but the value is from the last assignment.

Examples
Hello.
Hello. My name is Bob. I am 27. I am male.
Hello. I am 27. I am male. My name is Bob.
Hello. My name is Alice. I am female.
Hello. My name is Batman.
Task
Fix the code so we can all go home early.

class Dinglemouse(object):

    def __init__(self):
        self.name = None
        self.sex  = None
        self.age  = None

    def setAge(self, age):
        self.age = age
        return self

    def setSex(self, sex):
        self.sex = sex
        return self

    def setName(self, name):
        self.name = name
        return self

    def hello(self):
        return "Hello. My name is {}. I am {}. I am {}.".format(self.name, self.age, "male" if self.sex=='M' else "female")
"""


class Dinglemouse(object):

    def __init__(self):
        self.attributes = {}
        self.order = []

    def setAge(self, age):
        self.attributes['age'] = age
        if 'age' not in self.order:
            self.order.append('age')
        return self

    def setSex(self, sex):
        self.attributes['sex'] = sex
        if 'sex' not in self.order:
            self.order.append('sex')
        return self

    def setName(self, name):
        self.attributes['name'] = name
        if 'name' not in self.order:
            self.order.append('name')
        return self

    def hello(self):
        parts = ["Hello."]
        for attr in self.order:
            if attr == 'name':
                parts.append(f"My name is {self.attributes['name']}.")
            elif attr == 'age':
                parts.append(f"I am {self.attributes['age']}.")
            elif attr == 'sex':
                sex_str = "male" if self.attributes['sex'] == 'M' else "female"
                parts.append(f"I am {sex_str}.")
        return " ".join(parts)

