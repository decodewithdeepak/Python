import time  # Built-in Module
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')
print(timestamp)
timestamp = time.strftime('%M')
print(timestamp)
timestamp = time.strftime('%S')
print(timestamp)
# https://docs.python.org/3/library/time.html#time.strftime

# hour = int(input("Entr hour: "))

hour = int(time.strftime('%H'))
if (hour < 12):
    print("Good Morning")

elif (hour < 17):
    print("Good Afternoon")

elif (hour < 20):
    print("Good Evening")

else:
    print("Good Night")
