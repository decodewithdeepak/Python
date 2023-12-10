# Sorting in Python can be done by using the built-in sort() method, which uses the Timsort algorithm.
list = [10, 20, 4, 45, 99]
list.sort()
print("Largest element is:", list[-1])
print("Smallest element is:", list[0])


# Selection Sort Algorithm

def selection_sort(list):
    for i in range(len(list)):
        min_index = i

        for j in range(i + 1, len(list)):
            if list[min_index] > list[j]:
                min_index = j

        # Swap the minimum value with the compared value
        list[i], list[min_index] = list[min_index], list[i]

# Example usage:
my_list = [2, 7, 4, 1, 5, 3, 6, 9, 8]
selection_sort(my_list)
print(my_list)


# Insertion Sort Algorithm

def insertion_sort(list):
    for i in range(1, len(list)):
        j = i - 1
        next_element = list[i]

        # Compare the current element with next one

        while (list[j] > next_element) and (j >= 0):
            list[j + 1] = list[j]
            j = j - 1

        list[j + 1] = next_element

# Example usage:
my_list = [2, 7, 4, 1, 5, 3, 6, 9, 8]
insertion_sort(my_list)
print(my_list)


# Bubble Sort Algorithm

def bubble_sort(list):
    for i in range(len(list)):
        for j in range(len(list) - 1):
            if list[j] > list[j + 1]:
                # Swap the elements
                list[j], list[j + 1] = list[j + 1], list[j]

# Example usage:
my_list = [2, 7, 4, 1, 5, 3, 6, 9, 8]
bubble_sort(my_list)
print(my_list)
