import random

user_number = int(input("Pick a number from 1 - 100: "))
if user_number > 100 or user_number < 0:
    print("wrong input")
random_number = random.randrange(1, 101)