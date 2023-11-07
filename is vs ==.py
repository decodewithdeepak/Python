# The "is" keyword compares the exact location of object in memory
# While the "==" operator compares the values of object.
a = 5
b = 5
 
print(a == b)  # True
print(a is b)  # True

a = 4
b = "4"
 
print(a == b)  # False
print(a is b)  # False

a = "hello"
b = "hello"
 
print(a == b)  # True
print(a is b)  # True

a = (1, 2, 3)
b = (1, 2, 3)
 
print(a == b)  # True
print(a is b)  # True

# For mutable objects such as lists and dictionaries, is and == can behave differently

a = [1, 2, 3]
b = [1, 2, 3]
 
print(a == b)  # True
print(a is b)  # False

a = {1, 2, 3}
b = {1, 2, 3}
 
print(a == b)  # True
print(a is b)  # False
 

