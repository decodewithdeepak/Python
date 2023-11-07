# Lists are mutable
print("Sorting a list in ascending order:")
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)

num = [4, 2, 5, 3, 6, 1, 2, 1, 2, 8, 9, 7]
num.sort()
print(num)


print("Sorting a list in descending order:")
colors = ["voilet", "indigo", "blue", "green"]
colors.sort(reverse=True)
print(colors)

num = [4, 2, 5, 3, 6, 1, 2, 1, 2, 8, 9, 7]
num.sort(reverse=True)
print(num)


print("Reversing a list:")
colors = ["voilet", "indigo", "blue", "green"]
colors.reverse()
print(colors)

num = [4, 2, 5, 3, 6, 1, 2, 1, 2, 8, 9, 7]
num.reverse()
print(num)


print("Indexing in a list:")
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.index("green"))

num = [4, 2, 5, 3, 6, 1, 2, 1, 3, 2, 8, 9, 7]
print(num.index(3))


print("Counting in a list:")
colors = ["voilet", "green", "indigo", "blue", "green"]
print(colors.count("green"))

num = [4, 2, 5, 3, 6, 1, 2, 1, 3, 2, 8, 9, 7]
print(num.count(2))


print("Copying a list:")
colors = ["voilet", "green", "indigo", "blue"]
newlist = colors.copy()
print(colors)
print(newlist)


print("Appending to a list:")
colors = ["voilet", "indigo", "blue"]
colors.append("green")
print(colors)


print("Inserting in a list:")
colors = ["voilet", "indigo", "blue"]
#           [0]        [1]      [2]

colors.insert(1, "green")  # inserts item at index 1
# updated list: colors = ["voilet", "green", "indigo", "blue"]
#       indexs              [0]       [1]       [2]      [3]

print(colors)


print("Extending a list:")
# add a list to a list
colors = ["voilet", "indigo", "blue"]
rainbow = ["green", "yellow", "orange", "red"]
colors.extend(rainbow)
print(colors)


print("Concatenating two lists:")
colors = ["voilet", "indigo", "blue", "green"]
colors2 = ["yellow", "orange", "red"]
print(colors + colors2)
