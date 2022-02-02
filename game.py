#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#
import random 

#prompt the user
print("Rock, Paper, Scissors, Shoot!")
print("")

import os

user_name = os.getenv("PLAYER_NAME", default="Player One")

print("")
print("Well hello there, " + user_name)
print( "Prepare yourself, the time has come. Type either 'rock', 'paper', or 'scissors' below and try your luck against the computer")
print("")

#take the user input
user_play = input() 
#convert the user input into lowercase
user_play = user_play.lower()

#confirm the user made a valid selection 
if user_play != "rock" and user_play != "paper" and user_play != "scissors": 
    print("Next time, select either rock, paper, or scissors. Run the program again to give it another try") 
    quit()
else: 
    print("Bold move " + user_name + ", you went with " +  user_play)

#establish list of potential plays from the computer
computer_options = ["rock", "paper", "scissors"] 
computer_play = random.choice(computer_options)

#show the user what the computer played 
print("The computer chose " + computer_play)
print("")

#replaying if there's a tie
while user_play == computer_play:
    print("FREE RPS!!! To overtime we go...make another selection")
    user_play = input()
    user_play = user_play.lower()
    print(user_play + ", an inspiring choice")
    computer_options = ["rock", "paper", "scissors"] 
    computer_play = random.choice(computer_options)
    print("the computer went with " + computer_play)
    print("")
    quit()

#choosing a winner 
if user_play == "rock" and computer_play == "paper":
    print("Sorry, " + user_name + ", the computer got the best of you this time. Run the program again for a rematch.")
    quit()
elif user_play == "rock" and computer_play == "scissors":
    print("*computer bows his head, because he knows that he's been been beat*")
    quit()
elif user_play == "paper" and computer_play == "rock": 
    print("*computer bows his head, because he knows that he's been been beat*")
    quit()
elif user_play == "paper" and computer_play == "scissors": 
    print("Sorry, " + user_name + ", the computer got the best of you this time. Run the program again for a rematch.")
    quit()
elif user_play == "scissors" and computer_play == "rock":
    print("*computer bows his head, because he knows that he's been been beat*")
    quit()
elif user_play == "scissors" and computer_play == "paper": 
     print("Sorry, " + user_name + ", the computer got the best of you this time. Run the program again for a rematch.")
    
print("")
print("A war well waged. Well done, and please play again")







