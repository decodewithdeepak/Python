# Program 1: Compute the GCD of two numbers.
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))

# if num1 > num2:
#     num1, num2 = num2, num1 #Swapping

# for i in range(1, num1+1): #Range starts from 1 and ends at num1
#     if num1 % i == 0 and num2 % i == 0:
#         gcd = i

# print("GCD of", num1, "and", num2, "is: ", gcd)

# Program 2: Find the square root of a number (Newton‘s method)
# num = float(input("Enter a number: "))
# guess = num/2
# accuracy = 0.01

# while abs(guess*guess - num) >= accuracy:
#     guess = guess - ((guess**2) - num)/(2*guess)

# print("Square root of", num, "is: ", guess)

# Program 3: Exponentiation (power of a number)
# num = int(input("Enter a number: "))
# exp = int(input("Enter exponent: "))
# result = 1

# for i in range(exp):
#     result = result * num

# print(num, "raised to power", exp, "is: ", result)

# Program 4: Find the maximum of a list of numbers
# num = int(input("How many numbers do you want to enter? "))
# list = []

# for i in range(num):
#     list.append(int(input("Enter number: ")))

# max = list[0]

# for i in range(1, num):
#     if list[i] > max:
#         max = list[i]

# print("Maximum number is: ", max)

# Program 5: Linear search and Binary search
# Linear search
# num = int(input("How many numbers do you want to enter? "))
# list = []

# for i in range(num):
#     list.append(int(input("Enter number: ")))

# key = int(input("Enter number to search: "))
# flag = -1

# for i in range(num):
#     if list[i] == key:
#         print("Number found at index: ", i)
#         flag = 1
#         break

# if flag == -1:
#     print("Number not found!")

# Binary search
# num = int(input("How many numbers do you want to enter? "))
# list = []

# for i in range(num):
#     list.append(int(input("Enter number: ")))

# key = int(input("Enter number to search: "))
# flag = -1
# low = 0
# high = num-1

# while low <= high:
#     mid = int((low+high)/2)
#     if key == list[mid]:
#         print("Number found at index: ", mid)
#         flag = 1
#         break
#     elif key > list[mid]:
#         low = mid+1
#     else:
#         high = mid-1

# if flag == -1:
#     print("Number not found!")

# Program 6: Selection sort, Insertion sort
# # Selection sort
# num = int(input("How many numbers do you want to enter? "))
# list = []

# for i in range(num):
#     list.append(int(input("Enter number: ")))

# for i in range(num-1):
#     min = i
#     for j in range(i+1, num):
#         if list[j] < list[min]:
#             min = j
#     list[i], list[min] = list[min], list[i]

# print("Sorted list is: ", list)

# # Insertion sort
# num = int(input("How many numbers do you want to enter? "))
# list = []

# for i in range(num):
#     list.append(int(input("Enter number: ")))

# for i in range(1, num):
#     temp = list[i]
#     j = i-1
#     while j >= 0 and temp < list[j]:
#         list[j+1] = list[j]
#         j = j-1
#     list[j+1] = temp

# print("Sorted list is: ", list)

# Program 7: Merge sort
# num = int(input("How many numbers do you want to enter? "))
# list = []

# for i in range(num):
#     list.append(int(input("Enter number: ")))

# def mergeSort(list):
#     if len(list) > 1:
#         mid = len(list)//2
#         left = list[:mid]
#         right = list[mid:]

#         mergeSort(left)
#         mergeSort(right)

#         i = j = k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 list[k] = left[i]
#                 i = i+1
#             else:
#                 list[k] = right[j]
#                 j = j+1
#             k = k+1

#         while i < len(left):
#             list[k] = left[i]
#             i = i+1
#             k = k+1

#         while j < len(right):
#             list[k] = right[j]
#             j = j+1
#             k = k+1

# mergeSort(list)
# print("Sorted list is: ", list)

# Program 8: First n prime numbers
# num = int(input("Enter a number: "))
# count = 0
# i = 2

# while count < num:
#     flag = 0
#     for j in range(2, i):
#         if i % j == 0:
#             flag = 1
#             break
#     if flag == 0:
#         print(i)
#         count = count+1
#     i = i+1

# # Program 9: Multiply matrices
# row1 = int(input("Enter number of rows in matrix 1: "))
# col1 = int(input("Enter number of columns in matrix 1: "))
# row2 = int(input("Enter number of rows in matrix 2: "))
# col2 = int(input("Enter number of columns in matrix 2: "))
# matrix1 = []
# matrix2 = []
# result = []

# for i in range(row1):

#     matrix1.append([])
#     for j in range(col1):
#         matrix1[i].append(int(input("Enter element: ")))

# for i in range(row2):

#     matrix2.append([])
#     for j in range(col2):
#         matrix2[i].append(int(input("Enter element: ")))

# for i in range(row1):
#     result.append([])
#     for j in range(col2):
#         result[i].append(0)

# for i in range(row1):
#     for j in range(col2):
#         for k in range(row2):
#             result[i][j] = result[i][j] + matrix1[i][k] * matrix2[k][j]

# print("Resultant matrix is: ")
# for i in range(row1):
#     for j in range(col2):
#         print(result[i][j], end=" ")
#     print()




# Program 10: Programs that take command line arguments (word count)

# import sys

# def word_count(filename):
#     try:
#         with open(filename, 'r') as file:
#             text = file.read()
#     except FileNotFoundError:
#         print(f"{filename} not found.")
#         return

#     words = text.split()
#     print(f"The file {filename} has {len(words)} words.")

# if __name__ == "__main__":
#     if len(sys.argv) != 2:
#         print("Usage: python word_count.py <filename>")
#     else:
#         word_count(sys.argv[1])



# Program 11: Find the most frequent words in a text read from a file
# from collections import Counter
# import re

# def most_frequent_words(filename):
#     try:
#         with open(filename, 'r') as file:
#             text = file.read().lower()
#     except FileNotFoundError:
#         print(f"{filename} not found.")
#         return

#     words = re.findall(r'\b\w+\b', text)
#     counter = Counter(words)
#     most_common = counter.most_common(10)

#     print(f"The 10 most common words in {filename} are:")
#     for word, count in most_common:
#         print(f"{word}: {count}")

# if __name__ == "__main__":
#     filename = input("Enter a filename: ")
#     most_frequent_words(filename)

# # Program 12: Simulate elliptical orbits in Pygame
# import pygame
# import sys
# import math

# # Initialize Pygame
# pygame.init()

# # Constants
# WIDTH, HEIGHT = 800, 600
# CENTER = (WIDTH // 2, HEIGHT // 2)
# BACKGROUND_COLOR = (255, 255, 255)
# ORBIT_COLOR = (200, 200, 200)
# PLANET_COLOR = (0, 0, 255)
# PLANET_RADIUS = 10
# ORBIT_RADIUS_X = 150
# ORBIT_RADIUS_Y = 100

# # Pygame setup
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Elliptical Orbits")
# clock = pygame.time.Clock()

# def draw_orbit(surface, center, radius_x, radius_y):
#     pygame.draw.ellipse(surface, ORBIT_COLOR, [center[0] - radius_x, center[1] - radius_y, 2 * radius_x, 2 * radius_y], 1)

# def draw_planet(surface, center, angle, radius):
#     x = int(center[0] + radius * math.cos(angle))
#     y = int(center[1] + radius * math.sin(angle))
#     pygame.draw.circle(surface, PLANET_COLOR, (x, y), PLANET_RADIUS)

# def main():
#     angle = 0

#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()

#         screen.fill(BACKGROUND_COLOR)

#         # Draw the orbit
#         draw_orbit(screen, CENTER, ORBIT_RADIUS_X, ORBIT_RADIUS_Y)

#         # Calculate the position of the planet
#         planet_x = int(CENTER[0] + ORBIT_RADIUS_X * math.cos(math.radians(angle)))
#         planet_y = int(CENTER[1] + ORBIT_RADIUS_Y * math.sin(math.radians(angle)))

#         # Draw the planet
#         pygame.draw.circle(screen, PLANET_COLOR, (planet_x, planet_y), PLANET_RADIUS)

#         # Update the angle for the next frame
#         angle += 1

#         pygame.display.flip()
#         clock.tick(60)

# if __name__ == "__main__":
#     main()


# Program 13: Simulate bouncing ball in Pygame

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball parameters
ball_radius = 20
ball_speed = 5

# Function to draw the ball
def draw_ball(screen, x, y):
    pygame.draw.circle(screen, RED, (x, y), ball_radius)

# Main function
def main():
    # Set up the display
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Bouncing Ball Simulation")
    
    clock = pygame.time.Clock()

    # Initial ball position and velocity
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    ball_velocity_x, ball_velocity_y = ball_speed, ball_speed

    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update ball position
        ball_x += ball_velocity_x
        ball_y += ball_velocity_y

        # Bounce off the screen boundaries
        if ball_x - ball_radius < 0 or ball_x + ball_radius > WIDTH:
            ball_velocity_x = -ball_velocity_x
        if ball_y - ball_radius < 0 or ball_y + ball_radius > HEIGHT:
            ball_velocity_y = -ball_velocity_y

        # Clear the screen
        screen.fill(BLACK)

        # Draw the ball
        draw_ball(screen, int(ball_x), int(ball_y))

        # Update the display
        pygame.display.flip()

        # Cap the frame rate
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
