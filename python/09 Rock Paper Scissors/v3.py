import random

# from random import randint
print("Rock...")
print("Paper...")
print("Scissors...")


player = input("Player choice: ").lower()
rand_num = random.randint(0, 2)  # 0,2 because we need 3 random integers
if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
elif rand_num == 2:
    computer = "scissors"

print(f"Computer choice: {computer}")

if player == computer:
    print("Its a tie!!!!")

elif player == "rock":
    if computer == "scissors":
        print("player wins!")
    elif computer == "paper":
        print("computer wins!")

elif player == "paper":
    if computer == "rock":
        print("player wins!")
    elif computer == "scissors":
        print("computer wins!")

elif player == "scissors":
    if computer == "paper":
        print("player wins!")
    elif computer == "rock":
        print("computer wins!")

else:
    print("Please enter a valid choice")