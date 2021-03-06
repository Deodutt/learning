import random  # from random import randint
import getpass  # used to hide user input

# You need to install colorama. Run it in the powershell -> pip install colorama
from colorama import init
from colorama import Fore, Back, Style

init()

player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print(
        f"Player Score: {player_wins}/{winning_score} || Computer Score: {computer_wins}/{winning_score}"
    )
    print("Please enter your choice!")
    print("Rock...")
    print("Paper...")
    print("Scissors...")
    print("\n")

    player = getpass.getpass("Enter your choice: ").lower()
    if player == "quit" or player == "q":
        break
    print("\n")

    rand_num = random.randint(0, 2)  # 0,2 because we need 3 random integers
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    elif rand_num == 2:
        computer = "scissors"

    # showing computer's choice
    # print(f"Computer choice: {computer}")
    print(f"{Back.RED}Computer choice: {computer}")
    print(Style.RESET_ALL)

    # showing players's choice
    # print(f"Players choice: {player}")
    print(f"{Back.GREEN}Players choice: {player}")
    print(Style.RESET_ALL)

    print("\n\n")
    ##########

    if player == computer:
        # print("Its a tie!!!!")
        # print(Fore.RED + 'Its a tie!!!!')
        print(f"{Fore.RED}It's a TIE!!!")
        print(Style.RESET_ALL)

    elif player == "rock":
        if computer == "scissors":
            # print("player wins!")
            # print(Fore.GREEN + 'player wins!')
            print(f"{Fore.GREEN}player wins!")
            print(Style.RESET_ALL)
            player_wins += 1

        elif computer == "paper":
            # print("computer wins!")
            # print(Fore.RED + 'computer wins!')
            print(f"{Fore.RED}computer wins!")
            print(Style.RESET_ALL)
            computer_wins += 1

    elif player == "paper":
        if computer == "rock":
            # print("player wins!")
            # print(Fore.GREEN + 'player wins!')
            print(f"{Fore.GREEN}player wins!")
            print(Style.RESET_ALL)
            player_wins += 1

        elif computer == "scissors":
            # print("computer wins!")
            # print(Fore.RED + 'computer wins!')
            print(f"{Fore.RED}computer wins!")
            print(Style.RESET_ALL)
            computer_wins += 1

    elif player == "scissors":
        if computer == "paper":
            # print("player wins!")
            # print(Fore.GREEN + 'player wins!')
            print(f"{Fore.GREEN}player wins!")
            print(Style.RESET_ALL)
            player_wins += 1

        elif computer == "rock":
            # print("computer wins!")
            # print(Fore.RED + 'computer wins!')
            print(f"{Fore.RED}computer wins!")
            print(Style.RESET_ALL)
            computer_wins += 1

    else:
        # print("Please enter a valid choice")
        # print(Fore.RED + 'Please enter a valid choice')
        print(f"{Fore.RED}Please enter a valid choice")
        print(Style.RESET_ALL)

if player_wins > computer_wins:
    print(f"{Fore.GREEN}CONGRATS, YOU WON!")
    print(Style.RESET_ALL)

elif player_wins == computer_wins:
    print(f"{Fore.RED}It's a TIE!!!")
    print(Style.RESET_ALL)

else:
    print(f"{Fore.RED}Oh noooo :( The computer won!")
    print(Style.RESET_ALL)