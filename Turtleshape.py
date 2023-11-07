import turtle as t

# Draw a square of side 50 units
# for i in range(4):
#     t.forward(50) # Forward turtle by 50 units
#     t.right(90) # Turn turtle by 90 degrees

# t.done() # To hold the screen

# Draw a triangle of side 50 units
# for i in range(3):
#     t.forward(50) # Forward turtle by 50 units
#     t.right(120) # Turn turtle by 120 degrees

# t.done()

# Draw a circle of radius 50 units
# t.circle(50)

# t.done()

# Draw a regular polygon of any number of sides and length
# n = int(input("Enter number of sides: "))
# l = int(input("Enter length of each side: "))
# for i in range(n):
#     t.forward(l)
#     t.right(360/n)

# t.done()

# Draw a star
# for i in range(5):
#     t.forward(50)
#     t.right(144)

# t.done()

# Draw a archimedian circle spiral
# for i in range(100):
#     t.forward(i)
#     t.right(20)

# t.done()

# Draw a square spiral
for i in range(100):
    t.forward(i)
    t.right(90)

t.done()

