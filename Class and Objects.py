# Syntax: 
# class <ClassName>:
#     # Body of class (attributes and methods)

# ObjectName = ClassName()

class MyClass:
    x = 5

obj = MyClass()
print(obj.x)


class Person:
    name = "Deepak"
    occupation = "Software Developer"
    networth = 10

    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = Person()
b = Person()
c = Person()

a.name = "Shubham"
a.occupation = "Accountant"

b.name = "Nitika"
b.occupation = "HR"

# print(a.name, a.occupation)
a.info()
b.info()
c.info()


class Details:
    name = "Deepak"
    age = 20


obj1 = Details()
print(obj1.name)
print(obj1.age)


class Details:
    name = "Deepak"
    age = 20

    def desc(self):
        print("My name is", self.name, "and I'm", self.age, "years old.")


obj1 = Details()
obj1.desc()

