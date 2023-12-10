# Factorial using recursion

def factorial(n):
    if n < 0:
        return "Please enter a positive integer."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
n = int(input("Enter a number to find the factorial : "))
result = factorial(n)
print(f"The factorial of {n} is : {result}")


# Fibonacci series using recursion

def fibonacci(n):
    if n <= 0:
        return "Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
n = int(input("Enter the number of terms : "))
print("The fibonacci series is : ")
for i in range(1, n + 1):
    print(fibonacci(i), end = " ") # end = " " is used to print the output in a single line


# Sum of natural numbers using recursion

def sum_of_nat_num(n):
    if n < 0:
        return "Please enter a positive integer."
    elif n == 0:
        return 0
    else:
        return n + sum_of_nat_num(n - 1)
    
number = int(input("\nEnter a number upto which you want to find the sum of natural numbers : "))
result = sum_of_nat_num(number)
print(f"The sum of natural numbers upto {number} is : {result}")


# Sum of digits of a number using recursion

def sum_of_digits(n):
    if n < 0:
        return "Please enter a positive integer."
    elif n < 10:
        return n
    else:
        return n % 10 + sum_of_digits(n // 10)

number = int(input("Enter a number to find the sum of its digits : "))
result = sum_of_digits(number)
print(f"The sum of digits of {number} is : {result}")


# Binary Search using recursion

def binary_search(list, target, left, right):
    if left > right:
        return -1
    else:
        mid = (left + right) // 2
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            return binary_search(list, target, mid + 1, right)
        else:
            return binary_search(list, target, left, mid - 1)
        
my_list = [1, 2, 5, 7, 8, 10] # Sorted list
target = 8
result = binary_search(my_list, target, 0, len(my_list) - 1)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")


# Linear Search using recursion

def linear_search(list, target, index):
    if index == len(list):
        return -1
    elif list[index] == target:
        return index
    else:
        return linear_search(list, target, index + 1)
    
my_list = [10, 1, 5, 2, 8, 7]
target = 8
result = linear_search(my_list, target, 0)
if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")

