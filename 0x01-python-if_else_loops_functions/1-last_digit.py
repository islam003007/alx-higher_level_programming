#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
temp = number
if temp < 0:
    temp *= -1

if temp % 10 > 5:
    print(f"Last digit of {number} is {temp % 10} and is greater than 5")
elif temp % 10 == 0:
    print(f"Last digit of {number} is {temp % 10} and is 0")
else:
    print(f"Last digit of {number} is {temp % 10} \
and is less than 6 and not 0")
