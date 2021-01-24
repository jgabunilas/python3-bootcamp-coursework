# Dad joke generator
## Written by Jason Gabunilas

# Import dependencies

from pyfiglet import figlet_format
from termcolor import colored
from colorama import init
import random
import requests

init()

# Generate ascii art for dad joke generator main title
title_msg = figlet_format('DAD JOKE GENERATOR 5000')
colored_ascii = colored(title_msg, color = 'blue')

print(colored_ascii)

# Define a function to make the request from icanhazdadjoke
def retrieve_jokes(term):
    # Set the URL to icanhazdadjoke
    url = "https://icanhazdadjoke.com/search"
    response = requests.get(url, 
                            headers = {"Accept":"application/json"}, 
                            params = {
                                "term" : search_term,
                           })
    data = response.json()  
    # The returned response is a list of dictionaries, each dictionary containing an ID and a joke. 
    return data

# Initialize the joke generator loop and set continue_play to 'y'
generator_on = True
continue_play = 'y'

# The joke loop will continue so long as generator_on is True
while generator_on:
    if continue_play == 'y':
        search_term = input("Please choose a joke subject: ")
        
        # Call the retrieve_jokes function and return the json data that it retrieves
        data = retrieve_jokes(search_term)

        num_jokes = len(data['results'])
        
        # If the term returned no jokes, tell the user as such
        if num_jokes == 0:
            print(f"Your search for {search_term} generated no jokes. Please try again.")
            
        # Otherwise, inform the user how many jokes were returned and choose one at random to display.
        else:
            print(f"Your search for {search_term} generated {num_jokes} joke(s). Here is one:" )
            print(f"{random.choice(data['results'])['joke']}")
            
        # As the user if they would like to continue playing
        continue_play = input("Would you like another joke? (Please enter 'y' or 'n':) ")
        
    # If the user no longer wants to continue playing, exit the loop
    elif continue_play == 'n':
        generator_on = False
        print("Thank you. Goodbye!")
    # If the entry for continue_play is invalid, instruct the user to enter a valid input.
    else:
        continue_play = input("Entry invalid. Please enter 'y' or 'n'. Would you like another joke? ")