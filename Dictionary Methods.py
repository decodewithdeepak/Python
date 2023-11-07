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

