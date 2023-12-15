# Dictionary Methods
# clear() - Removes all the elements from the dictionary
# copy() - Returns a copy of the dictionary
# fromkeys() - Returns a dictionary with the specified keys and values
# get() - Returns the value of the specified key
# items() - Returns a list containing a tuple for each key value pair
# keys() - Returns a list containing the dictionary's keys
# pop() - Removes the element with the specified key
# popitem() - Removes the last inserted key-value pair
# setdefault() - Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update() - Updates the dictionary with the specified key-value pairs
# values() - Returns a list of all the values in the dictionary
# del - Deletes the dictionary

info = {'name': 'Deepak', 'age': 20, 'eligible': True}
print(info)
info.update({'age': 20})
info.update({'DOB': 2003})
print(info)

info = {'name': 'Karan', 'age': 19, 'eligible': True}
info.clear()  # removes all the items
print(info)

info = {'name': 'Karan', 'age': 19, 'eligible': True}
info.pop('age')  # removes the specific key-value pair
print(info)

info = {'name': 'Karan', 'age': 19, 'eligible': True}
info.popitem()  # removes the last key-value pair
print(info)

info = {'name': 'Karan', 'age': 19, 'eligible': True}
del info['age']  # to remove a dictionary item.
print(info)


info = {'name': 'Karan', 'age': 19, 'eligible': True, 'DOB': 2003}
del info  # will delete the dictionary entirely
# print(info)  # NameError: name 'info' is not defined

