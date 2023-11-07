print("Public Access Specifier :")


class Student:
    # constructor is defined
    def __init__(self, age, name):
        self.age = age               # public variable
        self.name = name             # public variable


obj = Student(21, "Harry")
print(obj.age)
print(obj.name)


print("\nPrivate Access Specifier :")


class Student:
    def __init__(self, age, name):
        self.__age = age      # An indication of private variable
        self.__name = name

class Subject(Student):
    pass


obj = Student(21, "Harry")

# print(obj.__age)  # can't be accessed diretly
print(obj._Student__age)  # can be accessed indiretly in the same class
print(obj.__dir__())


# cannot be accessed or inherited outside of class
obj1 = Subject
# print(obj1.__age) # AttributeError: 'subject' object has no attribute '__age'
# print(obj1._Subject__age)  # AttributeError

print("\nName mangling :")


class MyClass:
    def __init__(self):
        self._nonmangled_attribute = "I am a nonmangled attribute"
        self.__mangled_attribute = "I am a mangled attribute"


my_object = MyClass()

print(my_object._nonmangled_attribute)  # Output: I am a nonmangled attribute
# print(my_object.__mangled_attribute)  # Throws an AttributeError
print(my_object._MyClass__mangled_attribute)
# Output: I am a mangled attribute


print("\nProtected Access Specifier :")


class Student:
    def __init__(self):
        self._name = "Harry"

    def _funName(self):      # protected method
        return "CodeWithHarry"


class Subject(Student):  # inherited class
    pass


obj = Student()
# calling by object of Student class
print(obj._name)
print(obj._funName())
# print(dir(obj))

obj1 = Subject()
# calling by object of Subject class
print(obj1._name)
print(obj1._funName())
