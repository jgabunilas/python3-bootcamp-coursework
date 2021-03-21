# Exercise in file writing in which the function statistics() takes as an argument a file name and returns a dictionary with the number of lines, words, and characters in the file

def statistics(filename):
        with open(filename, 'r', encoding='utf-8') as my_file:
                # read the file
                # initiate the stats dictionary
                stats = {}

                # number of lines is equal to the length of the list from .readlines()
                num_lines = len(my_file.readlines())
                # print(num_lines) 

                # Reset the cursor to the beginning of the file
                my_file.seek(0)

                # number of words can be found by using the string split method

                num_words = len(my_file.read().split())
                # print(num_words)

                # Reset the cursor to the beginning of the file
                my_file.seek(0)
                num_chars = len(my_file.read())
                # print(num_chars)

                # Append data the dictionary
                stats['lines'] = num_lines
                stats['words'] = num_words
                stats['characters'] = num_chars

                return stats

statistics('story.txt')

## Alternative solution with fewer lines of code

#     def statistics(file_name):
#         with open(file_name) as file:
#             lines = file.readlines()
     
#         return { "lines": len(lines),
#                  "words": sum(len(line.split(" ")) for line in lines),
#                  "characters": sum(len(line) for line in lines) }