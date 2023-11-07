# Program 1: Compute the GCD of two numbers.
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if num1 > num2:
#     num1, num2 = num2, num1 #Swapping

# for i in range(1, num1+1): #Range starts from 1 and ends at num1
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i

# print("GCD of", num1, "and", num2, "is: ", gcd)

# Program 2: Find the square root of a number (Newton‘s method)
# num = float(input("Enter a number: "))
# guess = num/2
# accuracy = 0.01

# while abs(guess*guess - num) >= accuracy:
#     guess = guess - ((guess**2) - num)/(2*guess)

# print("Square root of", num, "is: ", guess)

# Program 3: Exponentiation (power of a number)
# num = int(input("Enter a number: "))
# exp = int(input("Enter exponent: "))
# result = 1

# for i in range(exp):
#     result = result * num

# print(num, "raised to power", exp, "is: ", result)

# Program 4: Find the maximum of a list of numbers
# num = int(input("How many numbers do you want to enter? "))
# list = []

# for i in range(num):
#     list.append(int(input("Enter number: ")))

# max = list[0]

# for i in range(1, num):
#     if list[i] > max:
#         max = list[i]

# print("Maximum number is: ", max)

# Program 5: Linear search and Binary search
# Linear search
# num = int(input("How many numbers do you want to enter? "))
# list = []

# for i in range(num):
#     list.append(int(input("Enter number: ")))

# key = int(input("Enter number to search: "))
# flag = -1

# for i in range(num):
#     if list[i] == key:
#         print("Number found at index: ", i)
#         flag = 1
#         break

# if flag == -1:
#     print("Number not found!")

# Binary search
# num = int(input("How many numbers do you want to enter? "))
# list = []

# for i in range(num):
#     list.append(int(input("Enter number: ")))

# key = int(input("Enter number to search: "))
# flag = -1
# low = 0
# high = num-1

# while low <= high:
#     mid = int((low+high)/2)
#     if key == list[mid]:
#         print("Number found at index: ", mid)
#         flag = 1
#         break
#     elif key > list[mid]:
#         low = mid+1
#     else:
#         high = mid-1

# if flag == -1:
#     print("Number not found!")

# Program 6: Selection sort, Insertion sort
# # Selection sort
# num = int(input("How many numbers do you want to enter? "))
# list = []

# for i in range(num):
#     list.append(int(input("Enter number: ")))

# for i in range(num-1):
#     min = i
#     for j in range(i+1, num):
#         if list[j] < list[min]:
#             min = j
#     list[i], list[min] = list[min], list[i]

# print("Sorted list is: ", list)

# # Insertion sort
# num = int(input("How many numbers do you want to enter? "))
# list = []

# for i in range(num):
#     list.append(int(input("Enter number: ")))

# for i in range(1, num):
#     temp = list[i]
#     j = i-1
#     while j >= 0 and temp < list[j]:
#         list[j+1] = list[j]
#         j = j-1
#     list[j+1] = temp

# print("Sorted list is: ", list)

# Program 7: Merge sort
# num = int(input("How many numbers do you want to enter? "))
# list = []

# for i in range(num):
#     list.append(int(input("Enter number: ")))

# def mergeSort(list):
#     if len(list) > 1:
#         mid = len(list)//2
#         left = list[:mid]
#         right = list[mid:]

#         mergeSort(left)
#         mergeSort(right)

#         i = j = k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 list[k] = left[i]
#                 i = i+1
#             else:
#                 list[k] = right[j]
#                 j = j+1
#             k = k+1

#         while i < len(left):
#             list[k] = left[i]
#             i = i+1
#             k = k+1

#         while j < len(right):
#             list[k] = right[j]
#             j = j+1
#             k = k+1

# mergeSort(list)
# print("Sorted list is: ", list)

# Program 8: First n prime numbers
# num = int(input("Enter a number: "))
# count = 0
# i = 2

# while count < num:
#     flag = 0
#     for j in range(2, i):
#         if i % j == 0:
#             flag = 1
#             break
#     if flag == 0:
#         print(i)
#         count = count+1
#     i = i+1

# Program 9: Multiply matrices

# Program 10: Programs that take command line arguments (word count)

# Program 11: Find the most frequent words in a text read from a file

# Program 12: Simulate elliptical orbits in Pygame

# Program 13: Simulate bouncing ball in Pygame