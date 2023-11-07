x = 4  # global variable
print(x)


def hello():
    x = 5  # local variable
    y = 1
    print(f"The local x is {x}")
    print("Hello Everyone")


print(f"The global x is {x}")
hello()
print(f"The global x is {x}\n")

# print(y)


x = 10  # global variable


def my_function():
    y = 5  # local variable
    print(y)


my_function()
print(x)
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function


# The global keyword

x = 10  # global variable


def my_function():
    global x
    x = 4  # this will change the value of the global variable x
    y = 5  # local variable
    print(y)

my_function()
print(x)  # prints 5
# print(y) # this will cause an error because y is a local variable and is not accessible outside of the function

