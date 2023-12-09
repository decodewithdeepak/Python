import threading
import time

def print_numbers():
    for i in range(1, 6):
        print(f"Number {i}")
        time.sleep(1)  # Sleep for 1 second

def print_letters():
    for letter in 'abcde':
        print(f"Letter {letter}")
        time.sleep(1)  # Sleep for 1 second

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()
