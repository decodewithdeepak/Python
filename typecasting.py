a = "1"
b = "2"

print(a + b)
# Concatenation of string 1 and 2 will be done

print(int(a)+int(b))
# Explicit Typecasting of string to integer

string = "15"
number = 5
string_number = int(string) # Explicit conversion of string to integer
# Throws an error if the string is not a valid integer

sum = number + string_number
print("The sum of both numbers is : ", sum)

c = 1.9
d = 8  # Implicit conversion to 8.0
print(c + d)
