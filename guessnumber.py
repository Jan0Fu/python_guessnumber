import random

random_number = random.randrange(1, 101)
user_number = 0

while user_number != random_number :
    user_number = int(input("Guess a number from 1 - 100: "))
    if type(user_number) == str :
        print("Not a number")
    elif user_number > 100 or user_number < 1:
        print("Wrong input!")
    elif user_number > random_number :
        print("Try lesser number")
    else :
        print("Try bigger number")

print("You won! its", random_number)
