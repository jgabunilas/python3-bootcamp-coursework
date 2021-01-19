# This exercise repeats the entered phrase until the phrase becomes "stop copying me", after which the the while loop is broken
phrase = input("Hey, how's it going? ")

while phrase != "stop copying me":
        print(phrase)
        phrase = input("")

print("UGH FINE YOU WIN")