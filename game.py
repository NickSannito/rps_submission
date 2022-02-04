#
# todo: write some Python code here to satisfy the exercise objectives
# ... https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md
#import os

from pickle import NONE


#create determine_winner function
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

#allow user to create their own username 
if __name__ == "__main__":
    
    import os

    user_name = os.getenv("PLAYER_NAME", default="Player One")

    #Welcome Message
    print("Hi " + user_name + ", ready to play some Rock Paper Scissors!? To try your luck against the computer, type either 'rock', 'paper', or 'scissors'. ")
        #take the user input
    user_play = input() 
        #convert the user input into lowercase
    user_play = user_play.lower()

        #confirm the user made a valid selection 
    if user_play != "rock" and user_play != "paper" and user_play != "scissors": 
            print("Next time, select either 'rock', 'paper', or 'scissors'. Run the program again to give it another try") 
            quit()
    else: 
            print("Inspiring choice " + user_name + ", you played " +  user_play + ".")

    #establish list of potential plays from the computer
    from random import choice
    computer_options = ["rock", "paper", "scissors"] 
    computer_play = choice(computer_options)
        
    print("What did the computer go with? Looks like..." + computer_play + "!")

    #determine winner
    winner = determine_winner(user_play, computer_play)

    #display results

    if winner == user_play: 
            print("Well played, " + user_name + ", well played indeed.")
            quit()
    elif winner == computer_play:
            print("Well it seems the computer got the best of you this time. Run the program again to give it another shot.")
            quit()
    else: 
            print("It's a tie! Run the program again for some overtime!")
            quit()


