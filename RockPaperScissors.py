import time
import random

user_choice = int()
pc_choice = int()
scoreboard = [0, 0]
options = ["rock", "paper", "scissors"]

answer = input("Welcome to RockPapersScissors!, are you excited? ").lower()
while answer != "yes":
    if answer == "no":
        print("And what are you doing here? well... Let's try again")
    else:
        print("I don't understand what you actually wrote, just type yes or no")
    answer = input("Welcome to RockPapersScissors!, are you excited? ").lower()

print("Perfect! Let's start")

while True:
    user_choice = input("Type rock, paper or scissors: ").lower()
    if user_choice != "rock" and user_choice != "paper" and user_choice != "scissors":
        print("That was not expected, you have to type rock, paper or scissors ")
        continue

    print("3...")
    time.sleep(1)
    print("2...")
    time.sleep(1)
    print("1...")
    time.sleep(1)

    pc_choice = random.randint(0, 2)
    print("User choice-", user_choice, " vs ", options[pc_choice], "-pc choice")
    if (options[pc_choice] == "rock" and user_choice == "rock") or (options[pc_choice] == "paper"and user_choice == "paper") or (options[pc_choice] == "scissors"and user_choice =="scissors"):
        print("That's a draw")
    elif (options[pc_choice] == "rock" and user_choice == "paper") or (options[pc_choice] == "paper" and user_choice == "scissors") or (options[pc_choice] == "scissors" and user_choice == "rock"):
        print("You won!!")
        scoreboard[0] += 1
    else:
        print("Ohh you lost!")
        scoreboard[1] += 1
    print("The scoreboard is ", scoreboard[0], "-",scoreboard[1])