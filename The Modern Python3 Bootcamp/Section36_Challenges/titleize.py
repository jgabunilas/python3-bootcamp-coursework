# This function accepts a string of words and returns a new string with the first letter of every word in the string capitalized


def titleize(input_string):

        # Split the string on whitespaces
        input_string_list = input_string.split()

        # Initialize a new list to put the capitalized words into
        capped_list = []

        # Iterate over each word in the list input_string_list
        for word in input_string_list:
                # Reconstruct the word by slicing the first letter and capitalizing it, then adding the remainder of the word
                word = word[0].upper() + word[1:]
                # Append the capitalized word to the capitalized word list
                capped_list.append(word)
        

        # Build the new string with the capitalized word list
        # Initialize an empty string
        new_string = ''
        # Iterate over each word in the caplitzed word list
        for word in capped_list:
                # Add teh word to the string, followed by an empty space
                new_string = new_string + word + ' '
        # The final word that was added will come with an extra empty space. Remove it with rstrip()
        return new_string.rstrip()

print(titleize('this is awesome'))
print(titleize('oNLy cAPITALIZe fIRSt'))