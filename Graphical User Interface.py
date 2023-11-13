# Graphical User Interfaces (GUI) allow users to interact with the computer
# Simple GUI-Based Programs can be created using the library Tkinter
# Tkinter is a library that comes with Python and is used to create GUIs

import tkinter as tk # Import the Tkinter Library

window = tk.Tk() # Create a Window
window.title("Python GUI Program") # Set the Title of the Window
# window.geometry("800x800") # Set the Size of the Window

# Create a Label Widget
label = tk.Label(text="Welcome to the Python GUI Program!")
label.pack() # Add the Label to the Window

label = tk.Label(window, text="Hello Tkinter!", font=("Arial Bold", 50), fg="red", bg="yellow")
label.pack()

# Create a Button Widget
button = tk.Button(text="Click Me!")
button.pack() # Add the Button to the Window

button = tk.Button(window, text="Click Me!", height=2, width=10, bg="purple", fg="white")
button.pack()

def clicked():
    label = tk.Label(window, text="Button was clicked!")
    label.pack()

button = tk.Button(window, text="Click Me!", command=clicked)
button.pack()

# Create a Text Entry Widget
entry = tk.Entry()
entry.pack() # Add the Text Entry to the Window

entry = tk.Entry(window, width=50, bg="light blue", fg="black")
entry.pack()

# Create a checkbutton Widget
checkbutton = tk.Checkbutton(text="Check Me!")
checkbutton.pack() # Add the Checkbutton to the Window

# Create a Radiobutton Widget
radiobutton = tk.Radiobutton(text="Select Me!")
radiobutton.pack() # Add the Radiobutton to the Window

# Create a Spinbox Widget
spinbox = tk.Spinbox(values=(1, 2, 3, 4, 5))
spinbox.pack() # Add the Spinbox to the Window

# Create a Scale Widget
scale = tk.Scale(from_=0, to=100)
scale.pack() # Add the Scale to the Window

# Create a Listbox Widget
listbox = tk.Listbox()
listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.insert(4, "C#")
listbox.insert(5, "JavaScript")
listbox.pack() # Add the Listbox to the Window

# Create a Menu Widget
menu = tk.Menu()
menu.add_command(label="File")
menu.add_command(label="Edit")
menu.add_command(label="View")
menu.add_command(label="Help")
window.config(menu=menu) # Add the Menu to the Window

# Input and Output with Entry Fields
def onClick():
    user_input = entry.get()  # Get text from the entry field
    result_label.config(text="You entered: " + user_input) # Display the input

label = tk.Label(window, text="Enter your name:")
label.pack()

entry = tk.Entry(window)
entry.pack()
button = tk.Button(window, text="Submit", command=onClick)
button.pack()
result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop() # Run the Window
