# Sets are UNORDERED collection of data items. Sets do not contain duplicate items.

info = {"Carla", 19, False, 5.9, 19}
print(info)
for item in info:
    print(item)

if "Carla" in info:
    print("Carla is present.")
else:
    print("Carla is absent.")


a = {}  # dictionary
print(type(a))

a = set()  # null set
print(type(a))
