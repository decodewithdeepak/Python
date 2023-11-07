# if-else Statements

tomatoPrice = 80
budget = 100
if (tomatoPrice <= budget):
    print("Alexa, add 1 kg Tomato to the cart.")
else:
    print("Alexa, do not add Tomato to the cart.")



age = int(input("Enter Your Age : "))
print("Your Age is ", age)

if (age > 18):
    print("You can Drive.")

else:
    print("You cannot Drive.")


# elif (else if) Statements

num = 0
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
else:
    print("Number is positive.")


# Nested if statements

num = int(input("Enter a Number : "))
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
