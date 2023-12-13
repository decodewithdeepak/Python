# Program to Check if a Number is Positive, Negative, or 0:
# Input a number
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print("Positive number.")
elif number < 0:
    print("Negative number.")
else:
    print("Zero.")


# Program to Calculate Sphere Properties:
import math

# Input radius of the sphere
radius = float(input("Enter the radius of the sphere: "))

# Calculate properties
diameter = 2 * radius
circumference = 2 * math.pi * radius
surface_area = 4 * math.pi * radius**2
volume = (4/3) * math.pi * radius**3

# Display results
print(f"Diameter: {diameter}")
print(f"Circumference: {circumference}")
print(f"Surface Area: {surface_area}")
print(f"Volume: {volume}")


# Program to Input Information for n Students:
# Input the number of students
n = int(input("Enter the number of students: "))

# Initialize lists to store information
names = []
reg_numbers = []
total_marks = []

# Input information for each student
for i in range(n):
    print(f"\nEnter details for Student {i + 1}:")
    names.append(input("Name: "))
    reg_numbers.append(input("Registration Number: "))
    total_marks.append(float(input("Total Marks: ")))

# Display information for each student
print("\nStudent Information:")
for i in range(n):
    print(f"Student {i + 1} - Name: {names[i]}, Registration Number: {reg_numbers[i]}, Total Marks: {total_marks[i]}")


# Program to Find the Best of Two Test Average Marks out of Three:
# Input test marks
test1 = float(input("Enter marks for Test 1: "))
test2 = float(input("Enter marks for Test 2: "))
test3 = float(input("Enter marks for Test 3: "))

# Calculate average marks for each pair
average1 = (test1 + test2) / 2
average2 = (test2 + test3) / 2
average3 = (test1 + test3) / 2

# Find the best average
best_average = max(average1, average2, average3)

# Display the result
print(f"The best average marks are: {best_average}")


# Program to Check if a Triangle is a Right Triangle:
# Input lengths of three sides of the triangle
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
c = float(input("Enter length of side c: "))

# Display the result
if (a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2):
    print("It is a right triangle.")
else:
    print("It is not a right triangle.")


# Python Code to Find the Factorial of a Number:
# Function to calculate factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Input a number
num = int(input("Enter a number: "))

# Calculate and display the factorial
result = factorial(num)
print(f"The factorial of {num} is: {result}")


# Program to check if a given number is a strong number:
def strong(n):
    # Find the sum of the factorial of the digits
    sum_of_factorial = 0
    for digit in str(n):
        sum_of_factorial += factorial(int(digit))

    if sum_of_factorial == n:
        print(f"{n} is a strong number.")
    else:
        print(f"{n} is not a strong number.")

# Input a number
num = int(input("Enter a number: "))
strong(num)

# Program to check if a given number is a armstrong number:
def armstrong(n):
    # Find the sum of the cube of the digits
    sum_of_cubes = 0
    for digit in str(n):
        sum_of_cubes += int(digit)**3

    if sum_of_cubes == n:
        print(f"{n} is an Armstrong number.")
    else:
        print(f"{n} is not an Armstrong number.")

# Input a number
num = int(input("Enter a number: "))
armstrong(num)

# Program to check if a given number is a palindrome:
def palindrome(n):
    # Reverse the number
    reversed_num = int(str(n)[::-1])

    if reversed_num == n:
        print(f"{n} is a palindrome.")
    else:
        print(f"{n} is not a palindrome.")

# Input a number
num = int(input("Enter a number: "))
palindrome(num)

# Program to Display the Longest Word in a Sentence:
# Input a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into words
words = sentence.split()

# Find the longest word
longest_word = max(words, key=len)

# Display the longest word and its length
print(f"The longest word is '{longest_word}' with length {len(longest_word)}")


# Program to Display the Last Six Characters of a String:
# Given string
string1 = "The breakfast is ready"

# Display the last six characters
print("Last six characters:", string1[-6:]) # output: Last six characters: ready


# Program to Display the Last Six Characters of Another String:
# Given string
string2 = "waiting for COVID-19 Third Phase"

# Display the last six characters
print("Last six characters:", string2[-6:]) # output: Last six characters: Phase


# Using String Methods on the Variable "data":
# Given string
data = "Python rocks!"

# Obtain a list of words in the string
word_list = data.split()

# Convert the string to uppercase
uppercase_data = data.upper()

# Locate the position of the string "rocks"
position_of_rocks = data.find("rocks")

# Replace the exclamation point with a question mark
modified_data = data.replace("!", "?")

# Display the results
print("List of words:", word_list)
print("Uppercase string:", uppercase_data)
print("Position of 'rocks':", position_of_rocks)
print("Modified string:", modified_data)


# Program to Capitalize Each Character in a Text File:
# Open the file for reading
fname = input("Enter file name: ")
with open(fname, "r") as file:
    content = file.read()

# Convert the content to uppercase
content = content.title() # title() method returns a string where the first character in every word is upper case

# Open the file for writing
with open(fname, "w") as file:
    file.write(content)


# Program to Count the Frequency of Words in a File:
# Open the file for reading
fname = input("Enter file name: ")
with open(fname, "r") as file:
    content = file.read()

# Split the content into words
words = content.split() # split() method returns a list of words in the string

# Create a dictionary to store word frequencies
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Display word frequencies
for word, count in word_count.items():
    print(f"{word}: {count} times")



# Counting Characters in a String using Dictionary:
# Input a string
string = input("Enter a string: ")

# Create a dictionary
char_count = {}

# Count the characters
for char in string:
    char_count[char] = char_count.get(char, 0) + 1

# Display the result
for char, count in char_count.items():
    print(f"{char}: {count} times")



# Generate a dictionary that contains (i:i*i) such that i is a number ranging from 1 to n.
# Input a number
n = int(input("Enter a number: "))
# Create a dictionary
my_dict = {}
# Add key-value pairs to the dictionary
for i in range(1, n + 1):
    my_dict[i] = i * i
# Display the dictionary
print(my_dict)


# Program to Find the Sum of All Values in a Dictionary:
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
# Initialize the sum
sum = 0
# Add each value to the sum
for value in my_dict.values():
    sum += value
# Display the sum
print(f"Sum: {sum}")


# Program to check for the presence of a key in the dictionary
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
# Input a key
key = input("Enter a key: ")
# Check if the key is present
if key in my_dict:
    print(f"{key} is present in the dictionary.")
else:
    print(f"{key} is not present in the dictionary.")

# Program to check for the presence of a value in the dictionary
my_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
# Input a value
value = int(input("Enter a value: "))
# Check if the value is present
if value in my_dict.values():
    print(f"{value} is present in the dictionary.")
else:
    print(f"{value} is not present in the dictionary.")

