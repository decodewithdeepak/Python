# Multithreading is a process of executing multiple threads simultaneously.
# A thread is a lightweight sub-process, the smallest unit of processing.
# Each thread runs parallely and independently of each other.
# Each thread has its own execution stack.
# A thread shares data and resources of the process to which it belongs.
# Threads are used to perform multiple tasks at the same time.

# We can use threading module to create and manage threads in Python.


import threading

def print_numbers():
    for i in range(1, 6):
        print(f"Number {i}")

def print_letters():
    for letter in 'abcde':
        print(f"Letter {letter}")

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()
# Since the threads run parallely, the output is not in order. So the output is different each time the program is executed.


# Sleeping Threads
# We can make a thread sleep for a specified amount of time using the sleep() method of the time module.
# The sleep() method takes the number of seconds as an argument.

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
# The output is in order now.


# Producer-Consumer Problem
# The producer-consumer problem is a classic example of a multi-process synchronization problem.
# It involves two processes, the producer and the consumer, who share a common buffer.
# The producer's job is to generate data and put it into the buffer.
# At the same time, the consumer is consuming the data (i.e. removing it from the buffer).
# The problem is to make sure that the producer won't try to add data into the buffer if it's full and that the consumer won't try to remove data from an empty buffer.
# The solution for the producer is to either go to sleep or discard data if the buffer is full.
# The next time the consumer removes an item from the buffer, it notifies the producer, who starts to fill the buffer again.
# In the same way, the consumer can go to sleep if it finds the buffer to be empty.
# The next time the producer puts data into the buffer, it wakes up the sleeping consumer.
# The solution can be reached by means of inter-process communication, typically using semaphores.

import threading
import time

shared_buffer = [] # Shared buffer between producer and consumer
lock = threading.Lock() # Lock object to synchronize the access of shared buffer

def producer():
    global shared_buffer
    for i in range(1, 6):
        with lock:
            shared_buffer.append(i)
            print(f"Produced: {i}")
        time.sleep(1)

def consumer():
    global shared_buffer
    for _ in range(5):
        with lock:
            if shared_buffer:
                item = shared_buffer.pop(0)
                print(f"Consumed: {item}")
        time.sleep(1)

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()