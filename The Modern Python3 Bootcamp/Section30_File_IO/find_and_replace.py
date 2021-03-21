# The find_and_replace() function takes as an argument a file name, a word to search for, and a replacement word. It replaces all instances of the word in the file with a replacement word.

def find_and_replace(filename, search_word, replacement_word):
        with open(filename, "r+", encoding='utf-8') as my_file:

                # Read in the original story string
                original = my_file.read()
                
                # Create the edited string using the string replace()
                new_story_text = original.replace(search_word, replacement_word) 

                # Use the write function to replace the old text with new text, moving the cursor to the beginning first
                my_file.seek(0)
                my_file.write(new_story_text)



find_and_replace("story.txt", "Alice", "Colt")

# Instructor's solution
#     def find_and_replace(file_name, old_word, new_word):
#         with open(file_name, "r+") as file:
#             text = file.read()
#             new_text = text.replace(old_word, new_word)
#             file.seek(0)
#             file.write(new_text)
#             file.truncate()