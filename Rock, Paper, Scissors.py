#Rock, Paper, Scissors Game
from random import randint

moves= ["rock", "paper", "scissors"]

while True:
    computer= moves[randint(0,2)]
    player= input("rock, paper or scissors? (or end the game) ").lower()
    if player== "end the game":
        print("the game is over")
        break
    elif player== computer:
        print("tie")
    elif player== "rock":
        if computer == "paper":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    elif player== "paper":
        if computer == "scissors":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    elif player== "scissors":
        if computer == "rock":
            print("You lose!", computer, "beats", player)
        else:
            print("You win!", player, "beats", computer)
    else:
        print("check your spelling.....")