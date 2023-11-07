# x=[1,2,3]
# print(dir(x))
# print(x.__add__)

# x=(1,2,3)
# print(dir(x))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person("John", 30)
print(p.__dict__)

print(help(Person))

# print(help(str))
