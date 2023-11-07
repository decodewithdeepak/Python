# Reading from a File
f = open('myfile1.txt', 'r')
contents = f.read()
print(contents)

# # Writing to a File
f = open('myfile1.txt', 'w')
f.write('Good Morning ')

f = open('myfile2.txt', 'w') # Create a file


# Appending to a file
f = open('myfile1.txt', 'a')
f.write('How are you ')

# Closing a File
f.close()



#  automatically close the file
with open('myfile1.txt', 'a') as f:
    f.write('Hey I am inside with you')

