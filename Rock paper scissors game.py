import random

def player_choice():
    choice = input("Choose rock, paper or scissors: ")
    return choice

def computer_choice():
    choice = random.randint(1, 3)
    if choice == 1:
        choice = "rock"
    elif choice == 2:
        choice = "paper"
    else:
        choice = "scissors"
    return choice

def win(player, computer):
    print("You chose: " + player)
    print("Computer chose: " + computer)
    if player == computer:
        print("Tie")
    elif player == "rock" and computer == "scissors":
        print("Player wins")
    elif player == "paper" and computer == "rock":
        print("Player wins")
    elif player == "scissors" and computer == "paper":
        print("Player wins")
    else:
        print("Computer wins")


player = player_choice()
computer = computer_choice()
win(player, computer)
