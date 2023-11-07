class Person:

    def __init__(self, name, occ):
        print("Hey I am a person")
        self.name = name
        self.occ = occ

    def info(self):
        print(f"{self.name} is a {self.occ}")


a = Person("Harry", "Developer")
b = Person("Divya", "HR")
a.info()
b.info()
# print(a.name)
# a.name = "Divya"
# a.occ = "HR"
# a.info()

print("\n")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)

print("\n")


# Parameterized Constructor in Python


class Details:
    def __init__(self, animal, group):
        self.animal = animal
        self.group = group


obj1 = Details("Crab", "Crustaceans")
print(obj1.animal, "belongs to the", obj1.group, "group.")


# Default Constructor in Python
class Details:
    def __init__(self):
        print("animal Crab belongs to Crustaceans group")


obj1 = Details()




