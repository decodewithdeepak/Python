lst1 = [1, 2, 2, 3, 5, 4, 6]
lst2 = ["Red", "Green", "Blue"]
print(lst1)
print(lst2)

details = ["Abhijeet", 18, "FYBScIT", 9.8]
print(details)

print("\n")

list = [3, 5, 6, "Harry", True, 6, 7, 2, 32, 345, 23]
# index 0  1  2     3       4   5  6  7   8   9   10
print(list)
print(type(list))
print(len(list))

print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])


print(list[-3])  # Negative index
print(list[len(list)-3])  # Positive index by adding len(marks)


if "Harry" in list:
    print("Yes")
else:
    print("No")

if 6 in list:
    print("Yes")
else:
    print("No")


# Same thing applies for strings as well!
if "Ha" in "Harry":
    print("Yes\n")


print(list[0:7])
print(list[5:-1])  # [5:10]

print(list[1:9])
print(list[1:9:3])  # jumps index by 3
# printing every 3rd consecutive value


print("List Comprehension")

lst = [i for i in range(10)]
print(lst)
lst = [i*i for i in range(10)]
print(lst)
lst = [i*i for i in range(10) if i % 2 == 0]
print(lst)



names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if (len(item) > 4)]
print(namesWith_O)


