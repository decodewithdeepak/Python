fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")

print(fruit[0])
print(fruit[1])
print(fruit[2])
print(fruit[3])
print(fruit[4])

print("\nSlicing\n")

# returns character at specified index

print(fruit[:])
print(fruit[0:len(fruit)]) # by default value

print(fruit[0:4])  # Slicing from Start , no nedd to write 0
print(fruit[4:])  # Slicing till End
print(fruit[:5])  # Slicing from Start
print(fruit[1:4])  # Slicing in between

print(fruit[0:-3])  # Slicing using negative index
print(fruit[0:len(fruit)-3])  # length is added automatically

print(fruit[-1:-3])  # no output as [4:2] is illogical
print(fruit[-3:-1])  # [2:4] makes sense

# Loop through a String
for i in fruit:
   print(i)


# Quick Quiz
nm="Harry"
print(nm[-4:-2])