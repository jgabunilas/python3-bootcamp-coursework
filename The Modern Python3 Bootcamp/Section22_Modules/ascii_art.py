from pyfiglet import figlet_format
from termcolor import colored
from colorama import init

init()

def print_art(msg, color):
	# The list of valid colors can be found by accessing the help() for termcolor
	valid_colors = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")

	# if the user did not provide a valid color, default to magenta
	if color not in valid_colors:
		color = "magenta"

	# use figlet_format from pyfiglet to create the ascii art
	ascii_art = figlet_format(msg)

	# color the ascii art
	colored_ascii = colored(ascii_art, color=color)

	# Remember that the ascii art will not print itself. You have to print it manually
	print(colored_ascii)


msg = input("What would you like to print? ")
color = input("What color? ")
print_art(msg, color)