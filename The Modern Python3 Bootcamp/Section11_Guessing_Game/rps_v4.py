# play rock paper scissors

# import the choice function from the random module
from random import choice

print("...rock...")
print("...paper...")
print("...scissors...")

# initialize the number of wins for player and computer
player_wins = 0
computer_wins = 0
# choose the number of games to be won for ultimate victory
winning_score = 3

# print the victory conditions
print(f"The first to {winning_score} wins is the victor!")

# we want the game to run so long as both the player and computer have less wins than the winning score. As soon as one of those is not True, the loop will exit
while player_wins < winning_score and computer_wins < winning_score:
        print(f"Player Score: {player_wins}")
        print(f"Computer Score: {computer_wins}")
        player = input("Player, choose 'rock', 'paper', or 'scissors': ")
        # make the entry lower case. Could also add the .lower() function to the end of the string above
        player = player.lower()

        # the computer will choose one entry from the provided list at random
        computer = choice(['rock','paper','scissors'])
        # check that player and computer are valid inputs
        if (player == 'paper' or player == 'rock' or player == 'scissors') and (computer == 'paper' or computer == 'rock' or computer == 'scissors'):
                print(f"Player chooses {player}.")
                print(f"Computer chooses {computer}.")
                print("SHOOT!")
                # check for tie game
                if player == computer:
                        print("Tie game")
                # check player victory conditions. If the player wins, print a message stating such and increment the number of player_wins by 1
                elif (player == 'rock' and computer == 'scissors') or (player == 'scissors' and computer == 'paper') or (player == 'paper' and computer == 'rock'):
                        print(f"{player} beats {computer}! Player wins!")
                        player_wins += 1
                # all other conditions aside from the above are victories for the computer. If the computer wins, print a message stating such and increment the number of computer_wins by 1
                else:
                        print(f"{computer} beats {player}! Computer wins!")
                        computer_wins += 1
        else:
                print("Invalid entry or entries.")

# print the victory messages
if player_wins > computer_wins:
        print(f"Player has won {winning_score} games and is the champion!")
        print(f"Final Scores... Player: {player_wins}   Computer: {computer_wins}")
elif computer_wins > player_wins:
        print(f"Computer has won {winning_score} games and is the champion!")
        print(f"Final Scores... Player: {player_wins}   Computer: {computer_wins}")

