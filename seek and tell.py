with open('myfile5.txt', 'r') as f:
    print(type(f))

    # Move to the 10th byte in the file
    f.seek(10)

    # Read the next 5 bytes
    data = f.read(5)
    print(data)

    # Save the current position
    current_position = f.tell()
    print(current_position)

    # Seek to the saved position
    f.seek(current_position)


with open('myfile6.txt', 'w') as f:
 f.write('Hello World!')
 f.truncate(5) # truncate the file to a specific size
 
with open('myfile6.txt', 'r') as f:
 print(f.read())
