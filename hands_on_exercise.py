"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi

print(pi)
print(type(pi))


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)

if i<50:
    print(i, 'is less than 50')
elif i>50:
    print(i, 'is is greater than 50')
else:
    print('i is 50')


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])

if picked_fruit == ('orange'):
    print('An', picked_fruit, 'is orange')
elif picked_fruit == ('strawberry'):
    print('A', picked_fruit, 'is red')
else:
    print('A', picked_fruit, 'is yellow')


# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.

def multiplier (a,b):
    answer = a * b
    return (answer)


# TODO: Now call the function a few times to calculate the following answers
result = multiplier(12,96)
print("12 x 96 =", result)
result = multiplier(48,17)
print("48 x 17 =", result)
result = multiplier(196523, 87323)
print("196523 x 87323 =", result)
