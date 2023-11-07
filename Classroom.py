# class A:
#     def display(self):
#         print("Welcome")

# class B(A):
#     def display(self):
#         print("Good Morning")

# obj1 = A()
# obj2 = B()
# obj1.display()
# obj2.display()


# class Car:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color

#     class Brand:
#         def __init__(self, brand):
#             self.brand = brand

#         def display(self, car):
#             print("Car name is :", car.name)
#             print("Car color is :", car.color)
#             print("Car brand is :", self.brand)

# car1 = Car("Fortuner", "Black")
# brand1 = car1.Brand("Toyota")
# brand1.display(car1)


class student:
    def __init__(self):
        self.__name = " "

    def getName(self):
        return self.__name
        
    def setName(self, name):
        self.__name = name
        
obj = student()
obj.setName("Deepak")
name = obj.getName()
print(name)
