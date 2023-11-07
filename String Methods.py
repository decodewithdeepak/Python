# Strings are immutable (doesn't change itself but give new string on modification)

str = "Deepak Modi!!!!"
print(str)
print(len(str))

print(str.upper())  # converts a string to upper case
print(str.lower())  # converts a string to lower case

# print(str.strip)
print(str.rstrip("!"))  # removes any trailing character


print(str.replace("Deepak", "Ritvik"))
# replaces all occurrences of a string with another string

print(str.split((" ")))
# splits the given string at the specified instance and returns the separated strings as list items.


blogHeading = "inroduction to pytHon"
print(blogHeading.capitalize())
# capitalize() method turns only the first character of the string to uppercase and the rest other characters of the string are turned to lowercase

str1 = "hello"
capStr1 = str1.capitalize()
print(capStr1)
str2 = "hello WorlD"
capStr2 = str2.capitalize()
print(capStr2)


str3 = "Welcome to the Console!!!"
print(str3.center(50))
print(str3.center(50, "."))
# aligns the string to the center

print(str3.count("e"))
# number of times the given value has occurred within the given string

print(str3.endswith("!!!"))
#  checks if the string ends with a given value. If yes then return True, else return False.
print(str3.endswith("to", 4, 10))


str4 = "He's name is Dan. He is an honest man."
print(str4.find("is"))
print(str4.index("Dan"))
print(str4.find("Daniel"))
# searches for the first occurrence of the given value

print(str4.index("Dan"))
# index() raises an exception if value is absent whereas find() does not
# print(str4.index("Daniel"))

str5 = "WelcomeToTheConsole"  # no punctuations
print(str5.isalnum())
str5 = "Welcome To The Console"
print(str5.isalnum())

str5 = "Welcome"
print(str5.isalpha())

str5 = "hello world"
print(str5.islower())
str5 = "WORLD HEALTH ORGANIZATION"
print(str5.isupper())


str1 = "We wish you a Merry Christmas"
print(str1.isprintable())
str1 = "We wish you a Merry Christmas\n"
print(str1.isprintable())

str1 = "    "  # using Spacebar
print(str1.isspace())
str2 = "\t"  # using Tab
print(str2.isspace())

str1 = "World Health Organization"
print(str1.istitle())
str2 = "To kill a Mocking bird"
print(str2.istitle())

str1 = "Python is a Interpreted Language"
print(str1.startswith("Python"))

str1 = "Python is a Interpreted Language"
print(str1.swapcase())

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())

