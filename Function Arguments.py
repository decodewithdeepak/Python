def name(fname, mname, lname):
    print("Hello", fname, mname, lname)


name("Deepak", "Barnwal", "Modi")


def name(fname, mname="Barnwal", lname="Modi"):
    print("Hello", fname, mname, lname)


name("Deepak")


def name(fname, mname, lname):
    print("Hello", fname, mname, lname)


name(mname="Barnwal", lname="Modi", fname="Deepak")


def average(a, b, c=1):
    print("The average is ", (a + b + c) / 2)


average(5, 6)


def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is: ", sum / len(numbers))


average(5, 6, 7, 1)


def average(*numbers):
    # print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)


avg = average(5, 6, 7, 1)
print("Average is: ", avg)


def name(**name):
  print(type(name))
  print("Hello", name["fname"], name["mname"], name["lname"])


name(mname="Barnwal", lname="Modi", fname="Deepak")

