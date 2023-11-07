#  os module in Python is a built-in library that provides a wide variety of functions for interacting with the operating system
import os
 
# Open the file in read-only mode
f = os.open("myfile.txt", os.O_RDONLY)
 
# Read the contents of the file
contents = os.read(f, 1024)
 
# Close the file
os.close(f)


# Open the file in write-only mode
f = os.open("myfile.txt", os.O_WRONLY)
 
# Write to the file
os.write(f, b"Hello Everyone !!")
 
# Close the file
os.close(f)

# Get a list of the files in the current directory
files = os.listdir(".")
print(files)  # Output: ['myfile.txt', 'otherfile.txt']

# Create a new directory (produces multiple folder)
if(not os.path.exists("data")):
  os.mkdir("data")

for i in range(0, 100):
    os.mkdir(f"data/Day{i+1}")

# Just Wow 💖




    
