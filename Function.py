def hello():  # Function definition
    print("Hello Everyone !")


hello()  # Function calling
hello()
hello()
hello()
hello()


def name(fname, lname):
    print("Hello", fname, lname)


name("Deepak", "Modi")



def calculateGmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)


a = 9
b = 8
calculateGmean(a, b)

c = 8
d = 74
calculateGmean(c, d)


def isGreater(a, b):
    if (a > b):
        print("First number is greater")
    else:
        print("Second number is greater or equal")


a = 9
b = 8
isGreater(a, b)


def isLesser(a, b):
    pass




import math

# sqrt computes the square root
square_root = math.sqrt(4)

print("Square Root of 4 is",square_root)

# pow() comptes the power
power = pow(2, 3)

print("2 to the power 3 is",power)
