# playing against the computer

# import the choice function from the random module
from random import choice

print("...rock...")
print("...paper...")
print("...scissors...")

# have the game run 3 times
for times_playing in range(0,3):
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
                # check player victory conditions
                elif (player == 'rock' and computer == 'scissors') or (player == 'scissors' and computer == 'paper') or (player == 'paper' and computer == 'rock'):
                        print(f"{player} beats {computer}! Player wins!")
                # all other conditions aside from the above are victories for the computer
                else:
                        print(f"{computer} beats {player}! Computer wins!")
        else:
                print("Invalid entry or entries.")


