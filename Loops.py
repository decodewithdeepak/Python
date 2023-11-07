print("Let's learn about for loop")

# iterating over a string:
name = 'Deepak'
for i in name:
    print(i)
#    print(i, end=", ")


# iterating over a list:
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)

#  iterating over a range
for i in range(5):  # i = [0-4]
    print(i)

for k in range(4, 9):  # i = [4-8]
    print(k)


#  third parameter of range (ie range(x, y, z))
for k in range(1, 12, 3):
    print(k)


print("Let's learn about while loop")
i = 0
while (i < 9):
    print(i)
    i += 1

print("\n")

count = 5
while (count > 0):
    print(count)
    count = count - 1

print("Else with While Loop")
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0')


print("Emulating do while loop in python using infinite while loop")
i = 0
while True:
    print(i)
    i = i+1
    if (i % 10 == 0):  # ACTING AS CONDITION
        break


while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:
        break
