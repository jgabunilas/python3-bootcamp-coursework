# Stupid guessing game written by Jason Gabunilas
import random

# Assign a random number to be guesed
random_number = random.randint(1,10)  # numbers 1 - 10
# As the user to guess a number
number_guess = int(input("Guess a number from 1 through 10 \n"))
# Set the playing variable to True
playing = True

# This loop will continue to run as long as playing is True
while playing == True:
        # Check  whether the guess is actually a number between 1 and 10. If it is, proceed.
        if number_guess <= 10 and number_guess > 0:
                        # If the user's guess is too low, tell them to guess higher. Then assign the new value to number_guess.
                        if number_guess < random_number:
                                print("Too low, guess a higher number")
                                number_guess = int(input(""))
                        # If the user's guess is too high, tell them to guess lower. THen assign teh new value to number_guess
                        elif number_guess > random_number:
                                print("Too high, guess a lower number")
                                number_guess = int(input(""))
                        # If the user's guess is correct, tell them so.
                        elif number_guess == random_number:
                                print(f"You guessed correctly! The number was {random_number}.")
                                # Ask the user if they want to play a new game
                                new_game = input("Would you like to play again (y/n)?\n")
                                # If the input is not "y" or "n", ask them to answer the question again until they say "y" or "n"
                                while new_game != "y" and new_game != "n":
                                        print("Invalid input.")
                                        new_game = input("Would you like to play again (y/n)?\n")  
                                # If they want to play again, assign a new random number and ask the player for an initial guess. This will send the user back to the beginning of the original while loop to play again.  
                                if new_game == "y":
                                        random_number = random.randint(1,10)
                                        number_guess = int(input("Guess a number from 1 through 10 \n"))
                                # If they do not want to play again, set playing = False to exit the loop and thank the user for playing
                                elif new_game == "n":
                                        playing = False
                                        print("Okay, thanks for playing!")
                        # else:
                        #         print("Invalid input. Exiting game.")
                        #         break
        # If the guess is not a number between 1 and 10, ask the user to input a valid guess. This will send the user back to the beginning of the while loop with a new number_guess
        else:
                number_guess = int(input("Invalid input. Please guess a number between 1 and 10. \n"))
