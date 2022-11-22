import random

user_number = int(input("Guess a number from 1 - 10: "))
if user_number > 10 or user_number < 0:
    print("Wrong input!")
random_number = random.randrange(1, 11)

if user_number == random_number :
    print("Jackpot!")

if user_number > random_number :
    print("Wrong!")
    user_number = input("Try lesser number: ")

if user_number < random_number :
    print("Wrong!")
    user_number = input("Try bigger number: ")
    if user_number == random_number :
        print("Jackpot!")
