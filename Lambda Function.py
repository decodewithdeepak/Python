# Function to double the input
def double(x):
    return x * 2

print(double(5))

# Lambda function to double the input
double = lambda x: x * 2
print(double(5))


cube = lambda x: x*x*x
print(cube(5))

avg = lambda x, y, z: (x + y + z) / 3
print(avg(3, 5, 10))


def apply(fx, value):
  return 6 + fx(value)

print(apply(cube , 2))
print(apply(lambda x: x * x , 2))


# Function to calculate the product of two numbers
def multiply(x, y):
   return x * y
# Lambda function to calculate the product of two numbers
lambda x, y: x * y


# Lambda function to calculate the product of two numbers,
# with additional print statement
lambda x, y: print(f'{x} * {y} = {x * y}')