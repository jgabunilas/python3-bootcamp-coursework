# Exercise in file writing in which the function copy() takes as arguments an existing file name and a new file name and copies the reversed contents of the first file to the second file


def copy_and_reverse(old_filename, new_filename):
        with open(old_filename, 'r', encoding='utf-8') as file1:
                contents = file1.read()
                contents_reversed = contents[::-1]
        with open(new_filename, 'w', encoding='utf-8') as file2:
                file2.write(contents_reversed)

copy_and_reverse('story.txt','story_copy_reversed.txt')