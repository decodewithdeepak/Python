import turtle as t

t.title("My Turtle Program") # Set the title of the turtle screen
t.bgcolor("lightblue")# Set the background color of the turtle screen
t.setup(500, 500) # Set the dimensions of the turtle screen

t.color("red") # Set the color of the turtle pen
t.pensize(5) # Set the width of the turtle pen
t.speed(1) # Set the speed of the turtle pen

t.shape("turtle") # Set the shape of the turtle pointer
t.hideturtle() # Hide the turtle pointer

# Draw a square of side 100 units
for i in range(4):
    t.forward(100) # Forward turtle by 50 units
    t.right(90) # Turn turtle by 90 degrees

t.done() # To hold the screen
