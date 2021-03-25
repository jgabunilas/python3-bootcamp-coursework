# This function takes a first and last name and searches for a user with that first and last name in the csv file. If found, returns the index where the user is found. Otherwise returns a message stating the user wasn't found

from csv import DictReader

def find_user(first_name, last_name):
        with open("users.csv", 'r') as file:
                # create the csv_reader object
                csv_reader = DictReader(file)

                # Initialize the row index counter
                row_index = 1

                # Iterate through each OrderedDict item and check whether the First Name and Last Name keywords match the values given to the function
                for row in csv_reader:
                        # If there is a match, return the current row index
                        if row["First Name"] == first_name and row["Last Name"] == last_name:
                                return row_index
                        # If there is no match on this row, increment the index and move to the next row
                        row_index += 1
                # If there were no matches on any row, return the message that the user was not found.
                return "{} {} not found.".format(first_name, last_name)

print(find_user("Ryan", "Gosling"))
print(find_user("Alan", "Turing"))
print(find_user("Colt", "Steele"))

## Alternative solution using the enumerate function:

# def find_user(first_name, last_name):
#     with open("users.csv") as csvfile:
#         csv_reader = csv.reader(csvfile)
#         for (index, row) in enumerate(csv_reader):
#             first_name_match = first_name == row[0]
#             last_name_match = last_name == row[1]
#             if first_name_match and last_name_match:
#                 return index
#         return "{} {} not found.".format(first_name, last_name)