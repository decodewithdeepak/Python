# Linear Search Algorithm

def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i  # Return the index if the target is found
    return -1  # Return -1 if the target is not found

# Example usage:
my_list = [10, 1, 5, 2, 8, 7]
target = 8

result = linear_search(my_list, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")


# Binary Search Algorithm

def binary_search(list, target):
    # Set the left and right bounds
    left = 0
    right = len(list) - 1

    while left <= right:
        mid = (left + right) // 2  # Find the mid-value

        if list[mid] == target:
            return mid  # Return the index if the target is found
        elif list[mid] < target:
            left = mid + 1  # Continue searching towards the right
        else:
            right = mid - 1  # Continue searching towards the left

    return -1  # Return -1 if the target is not found

# Example usage:
my_list = [1, 2, 5, 7, 8, 10] # Sorted list
target = 8

result = binary_search(my_list, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list")

