import random

number = random.randint(0,100)

answer = input("Welcome to GuessTheNumber!, are you excited? ").lower()
i=1

while answer != "yes":
  if answer == "no":
    print("And what are you doing here? well... Let's try again")
  else:
    print("I don't understand what you actually wrote, just type yes or no")
  answer = input("Welcome to GuessTheNumber!, are you excited? ").lower()
 
print("Perfect! Let's start")
print("I'm thinking a number... mmmmmm... Aha! I got it")
print("The number is between 0 and 100 included")

userNumber=int(input("Your number is -->"))
while userNumber != number:
  i = i+1
  if userNumber > number:
    print("lower")
  elif userNumber < number:
    print("higher")
  userNumber=int(input("Your number is -->"))
print("Congratulations!! You found the number!")
print("Your score is ",i)