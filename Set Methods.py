# A set is mutable, i.e., we can remove or add elements to it. Set in python is similar to mathematical sets.

print("\nUnion : ")
# The union() and update() methods prints all items that are present in the two sets.
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities1.union(cities2)  # returns a new set
print(cities3)

cities1.update(cities2)  # adds item into the existing set from another set
print(cities1)


print("\nIntersection : ")
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities1.intersection(cities2)
print(cities3)

cities1.intersection_update(cities2)
print(cities1)


print("\nSymmetric Difference : ")
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities1.symmetric_difference(cities2)
print(cities3)

cities1.symmetric_difference_update(cities2)
print(cities1)

print("\nDifference : ")
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
cities3 = cities1.difference(cities2)
print(cities3)

cities1.difference_update(cities2)
print(cities1)


print("\nisdisjoint : ")
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities1.isdisjoint(cities2))

print("\nissuperset : ")
cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities1.issuperset(cities2))
cities3 = {"Delhi", "Madrid", "Berlin"}
print(cities1.issuperset(cities3))


print("\nissubset : ")

cities1 = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Delhi", "Madrid"}
print(cities2.issubset(cities1))

print("\nAdd() : ")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("Helsinki")
print(cities)


print("\nUpdate() : ")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Helsinki", "Warsaw", "Seoul"}
cities.update(cities2)
print(cities)


print("\nremove()/discard() : ")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}

# cities.remove("Tokyo")
# print(cities)

cities.discard("Tokyo")
print(cities)

# cities.remove("Seoul")
# print(cities) # KeyError: 'Seoul'

cities.discard("Seoul")
print(cities)


print("\npop()/del/clear() : ")
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# del cities  # delete the entire set
# print(cities)  # nameerror
cities.clear()
print(cities)


