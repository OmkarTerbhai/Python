# Input and Output in Python
import random
from enum import Enum


class Move(Enum) :
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

player = int(input("Enter your move:   \n1. Rock\n2.Paper\n3.Scissor \n"));
computer = int(random.choice("123"));

print("You chose : " + str(Move(player)).replace("Move.", ""));
print("Computer  chose : " + str(Move(computer)).replace("Move.", ""));

if computer == player :
    print("It's a Tie 🆗");

elif computer == 1 and player == 2 :
    print("You won 🎉");

elif computer == 2 and player == 3 :
    print("You won 🎉");

elif computer == 1 and player == 3 :
    print("You won 🎉");

else :
    print("Computer won 🤖")
