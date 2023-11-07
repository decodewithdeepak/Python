# Dictionaries are ordered collection of data items. Key-value Pairs
info = {'name': 'Deepak', 'age': 20, 'eligible': True}
print(info)

print(info['name'])  # Accessing single values
print(info.get('name'))  # better way


# print(info['roll'])  # KeyError: 'roll'
print(info.get('roll'))  # None

print(info.keys())  # Accessing keys
print(info.values())  # Accessing multiple values
print(info.items())  # Accessing key-value pairs


for key in info.keys():    # Accessing values using loop
    print(info[key])


for key in info.keys():  # Accessing key-value pairs using loop
    print(f"The value corresponding to the key {key} is {info[key]}")


for key, value in info.items():
    print(f"The value corresponding to the key {key} is {value}")
