print('''Tuples are immutable, hence if you want to add, remove or change tuple items, then first you must convert the tuple to a list. Then perform operation on that list and convert it back to tuple.''')

countries = ("India", "Italy", "Spain", "England", "Germany")
temp = list(countries)
temp.append("Russia")  # add item
temp.pop(3)  # remove item
temp[2] = "Finland"  # change item
countries = tuple(temp)
print(countries)

# we can directly concatenate two tuples without converting them to list.
countries1 = ("India", "Vietnam", "China")
countries2 = ("Pakistan", "Afghanistan", "Bangladesh", "ShriLanka")

southEastAsia = countries1 + countries2
print(southEastAsia)


tuple1 = (0, 1, 2, 3, 2, 3, 1, 3, 2)
print('Count of 3 in Tuple1 is:', tuple1.count(3))
print('First occurrence of 3 is', tuple1.index(3))


