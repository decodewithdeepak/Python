# Tuples are immutable(unchangeable) meaning we can not alter them after creation.
tup = (1, 2, 76, 342, 32, "green", True)
print(type(tup), tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])

tup2 = tup[1:4]  # new Tuple is created as original tuple can't be altered
print(tup2)

if 342 in tup:
    print("Yes 342 is present in this tuple\n")


tuple1 = (1, 2, 2, 3, 5, 4, 6)
tuple2 = ("Red", "Green", "Blue")
print(tuple1)
print(tuple2)

details = ("Abhijeet", 18, "FYBScIT", 9.8)
print(details)

print("\n# Positive Indexing:")
country = ("Spain", "Italy", "India",)
# index      [0]      [1]      [2]
print(country[0])
print(country[1])
print(country[2])

print("\n# Negative Indexing:")
country = ("Spain", "Italy", "India", "England", "Germany")
#            [0]      [1]      [2]       [3]        [4]
print(country[-1])  # Similar to print(country[len(country) - 1])
print(country[-3])
print(country[-4])

print("\n# Check for item:")

country = ("Spain", "Italy", "India", "England", "Germany")
if "Germany" in country:
    print("Germany is present.")
else:
    print("Germany is absent.")


if "Russia" in country:
    print("Russia is present.")
else:
    print("Russia is absent.")


print("\n# Range of Index:")
animals = ("cat", "dog", "bat", "mouse", "pig",
           "horse", "donkey", "goat", "cow")
# Printing elements within a particular range:
print(animals[3:7])  # using positive indexes
print(animals[-7:-2])  # using negative indexes

#  Printing all element from a given index till the end
print(animals[4:])  # using positive indexeszzz
print(animals[-4:])  # using negative indexes

# printing all elements from start to a given index
print(animals[:6])  # using positive indexes
print(animals[:-3])  # using negative indexes


#  Print alternate values
print(animals[::2])  # using positive indexes
print(animals[-8:-1:2])  # using negative indexes


#  printing every 3rd consecutive withing given range
print(animals[1:8:3])
