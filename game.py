#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#import os

from pickle import NONE


def determine_winner(user_choice, computer_choice):
    """
    Determines the winning choice between two valid choices from selectable options: "rock", "paper", or "scissors".

    Returns the winning choice (e.g. "paper"), or None if there is a tie.

    Example: determine_winner("rock", "paper")
    """
    
    if user_choice == computer_choice: 
        winner = None
    elif user_choice == "rock" and computer_choice == "paper":
        winner = computer_choice 
    elif user_choice == "rock" and computer_choice == "scissors": 
        winner = user_choice
    elif user_choice == "paper" and computer_choice == "rock":
        winner = user_choice 
    elif user_choice == "paper" and computer_choice == "scissors": 
        winner = computer_choice
    elif user_choice == "scissors" and computer_choice == "rock":
        winner = computer_choice 
    elif user_choice == "scissors" and computer_choice == "paper": 
        winner = user_choice

    return winner

if __name__ == "__main__":
    
    import os

    user_name = os.getenv("PLAYER_NAME", default="Player One")

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
    from random import choice
    computer_options = ["rock", "paper", "scissors"] 
    computer_play = choice(computer_options)
    
    print("The computer chose" + computer_play)

    #determine winner
    winner = determine_winner(user_play, computer_play);

    #display results

    # TO DO FROM INSTRUCTIONS ON GITBHUB

    if winner == user_play: 
        print("congratulations! you won")
    elif winner == computer_play:
        print("Sorry, better luck next time.")
    else: 
        print("It's a tie!")


