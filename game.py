#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#import os

def determine_winner(choice_1, choice_2):
    """
    Determines the winning choice between two valid choices from selectable options: "rock", "paper", or "scissors".

    Returns the winning choice (e.g. "paper"), or None if there is a tie.

    Example: determine_winner("rock", "paper")
    """
    
    winner = "rock"

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

    #determine winner
    winner = determine_winner(user_play, computer_play);

    #display results

    # TO DO FROM INSTRUCTIONS ON GITBHUB

    print("Rock won! Driver function. Change later.")

