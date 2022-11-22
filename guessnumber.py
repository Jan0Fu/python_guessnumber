import random

random_number = random.randrange(1, 11)
user_number = 0

def new_input() :
    user_number = int(input("You have 3 attempts, guess a number from 1 - 10: "))
    if user_number > 10 or user_number < 0:
        print("Wrong input!")
    if type(user_number) == str :
        print("Not a number")

new_input()

def checker() :
    if  user_number < random_number :
        print(("Wrong! Try bigger number: "))
    elif user_number > random_number :
        print("Wrong! Try lesser number: ")
    else :
        print("Jackpot!")

checker()


if user_number > random_number :
    print("Wrong!")
    user_number = int(input("Try lesser number: "))
    if user_number == random_number :
        print("Jackpot!")
    if user_number > random_number :
        print("Wrong!")
        user_number = int(input("Try lesser number: "))
        if user_number == random_number :
            print("Jackpot!")
    if user_number < random_number :
        print("Wrong!")
        user_number = int(input("Try bigger number: "))
        if user_number == random_number :
            print("Jackpot!")


if user_number < random_number :
    print("Wrong!")
    user_number = int(input("Try bigger number: "))
    if user_number == random_number :
        print("Jackpot!")
    if user_number > random_number :
        print("Wrong!")
        user_number = int(input("Try lesser number: "))
        if user_number == random_number :
            print("Jackpot!")
    if user_number < random_number :
        print("Wrong!")
        user_number = int(input("Try bigger number: "))
        if user_number == random_number :
            print("Jackpot!")
