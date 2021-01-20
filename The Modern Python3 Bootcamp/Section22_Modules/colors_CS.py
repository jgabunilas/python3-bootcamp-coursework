from termcolor import colored
from colorama import init

init()

text = colored("HI THERE!", color="magenta", on_color="on_cyan", attrs=["blink"])
print(text)

