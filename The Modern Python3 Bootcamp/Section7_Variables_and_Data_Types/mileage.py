# The input function changes the prompt in the command line and waits for the user to enter something. We need to store the value in a variable that we can later use
print("How many kilometers did you cycle today?")
kilometers = input()
# The input function automatically saves the input as a string. That is why the concacenation below works. If it was not a string and was a number instead, you would not be able to do the concatenation.
print("Ok, you said " + kilometers + "kilometers") 
# But! We need to do some math on this. So the km being a string is problematic. So we need to turn kilometers into a float before we convert to miles. There are 1.60934 kilometers in a mile
miles = float(kilometers)/1.60934
# Now remember that this will give you miles as a float. You will need to either convert miles to a string OR use f-strings
# We probably also want to round this so we don't get a ton of decimal points. We can do this with the round() function! It takes two arguments: the value to be rounded, and the number of decimals to round to.
miles_rounded = round(miles, 2)
print(f"Your {kilometers} kilometer ride is equivalent to {miles_rounded} miles!")

print("This is fun!")