import random

random_number = random.randrange(1, 101)
user_number = 0
attempts = 8

while user_number != random_number :
    user_number = int(input("Guess a number from 1 - 100: "))
    if attempts == 1 :
        print("Game over!")
        break
    elif user_number > 100 or user_number < 1:
        print("Wrong input!")
    elif user_number > random_number :
        attempts = attempts - 1
        print("Try lesser number, attempts: ", attempts)
    elif user_number < random_number :
        attempts = attempts - 1
        print("Try bigger number, attempts: ", attempts)
    else :
        user_number == random_number
        print("Jackpot! Its number:",random_number, "You won!")

print("Number was", random_number)