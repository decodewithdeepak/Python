def cube(x):
    return x*x*x


print(cube(2))

l = [1, 2, 4, 6, 4, 3,]

# Using for loop
newl = []
for item in l:
    newl.append(cube(item))

print(newl)

# Another approach is MAPPING
newl = list(map(cube, l))
print(newl)

# FILTER


def filter_function(a):
    return a > 4


newnewl = list(filter(filter_function, l))
print(newnewl)

print("\n")

# Using lambda function

numbers = [1, 2, 3, 4, 5]  # List of numbers

# Double each number using the map function
doubled = map(lambda x: x * 2, numbers)

# Print the doubled numbers
print(list(doubled))


# Get only the even numbers using the filter function
evens = filter(lambda x: x % 2 == 0, numbers)

# Print the even numbers
print(list(evens))

from functools import reduce
 
# List of numbers
numbers = [1, 2, 3, 4, 5]
 
# Calculate the sum of the numbers using the reduce function
sum = reduce(lambda x, y: x + y, numbers)
 
# Print the sum
print(sum)
