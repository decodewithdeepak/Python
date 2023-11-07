print("Else with For Loop:")

for x in range(5):
    print(f"iteration no {x+1} in for loop")
#    print ("iteration no {} in for loop".format(x+1))
else:
    print("else block in loop")
print("Out of loop\n")


for i in range(6):
    print(i)

else:
    print("No value of i")


for i in range(6):
    print(i)
    if i == 4:
        break  # termination of loop
else:
    print("No value of i")  # not executed


print("\nElse with While Loop:")
x = 5
while (x > 0):
    print(x)
    x = x - 1
else:
    print('counter is 0\n')


i = 0
while (i <= 6):
    print(i)
    i = i+1

else:
    print("No value of i")


i = 0
while (i <= 6):
    print(i)
    i = i+1
    if i == 4:
        break  # termination of loop
else:
    print("No value of i")  # not executed
