# My solution
# import random

# random_number = random.randint(1, 10)  # numbers 1 - 10

# guess = int(input("Guess a number between 1 and 10: "))
# while guess != random_number:
#     if guess > random_number:
#         print("Too high, try again!!")
#     else:
#         print("Too low, try again!")
#     guess = int(input("Guess a number between 1 and 10: "))
# print("You guessed it! You won!")

###################################

# My Solution 2
# import random

# state = "y"
# while state != "n":
#     random_number = random.randint(1, 10)  # numbers 1 - 10
#     guess = int(input("Guess a number between 1 and 10: "))
#     while guess != random_number:
#         if guess > random_number:
#             print("Too high, try again!!")
#         else:
#             print("Too low, try again!")
#         guess = int(input("Guess a number between 1 and 10: "))
#     print("You guessed it! You won!")
#     state = str(input("Do you want to keep playing?: "))

###################################

# Colts Solution

import random

random_number = random.randint(1, 10)  # numbers 1 - 10


guess = ""

while guess != random_number:
    guess = input("Pick a number from 1 to 10: ")
    guess = int(guess)
    if guess < random_number:
        print("Too Low!")

    elif guess > random_number:
        print("Too HIGH!")
    else:
        print("You Won!")

print(random_number)
# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!