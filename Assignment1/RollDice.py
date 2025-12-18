# 3. Roll a dice 10 times using random.randint() and count how many times you get 6.

import random

def dice():
    count = 0
    for i in range(10):
        r = random.randint(1, 6)
        print("Roll:", r)
        if r == 6:
            count += 1
    return count

print("Six came:", dice(), "times")


'''
Output:
Roll: 6
Roll: 4
Roll: 1
Roll: 5
Roll: 3
Roll: 5
Roll: 2
Roll: 3
Roll: 4
Roll: 6
Six came: 2 times
'''