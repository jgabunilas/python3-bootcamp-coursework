import random

print("...rock...")
print("...paper...")
print("...scissors...")

player1 = input("(enter Player 1's choice): ")
player2 = input("(enter Player 2's choice): ")

# player1 = random.choice(['rock','paper','scissors'])
# player2 = random.choice(['rock','paper','scissors'])
# check that player1 and player2 are valid inputs
if (player1 == 'paper' or player1 == 'rock' or player1 == 'scissors') and (player2 == 'paper' or player2 == 'rock' or player2 == 'scissors'):
        print(f"Player 1 chooses {player1}")
        print(f"Player 2 chooses {player2}")
        print("SHOOT!")
        # check for tie game
        if player1 == player2:
                print("Tie game")
        # check player1 victory conditions
        elif (player1 == 'rock' and player2 == 'scissors') or (player1 == 'scissors' and player2 == 'paper') or (player1 == 'paper' and player2 == 'rock'):
                print(f"{player1} beats {player2}! Player 1 wins!")
        # all other conditions aside from the above are tie conditions
        else:
                print(f"{player2} beats {player1}! Player 2 wins!")
else:
        print("Invalid entry or entries")
