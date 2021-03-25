# Prints out the first and last names of the users in the users.csv file to the console

from csv import reader

def print_users():
        with open("users.csv", 'r') as file:
                # move the cursor to the beginning of the file
                file.seek(0)

                # create the csv_reader object
                csv_reader = reader(file)
                # skip the header row
                next(csv_reader)
                for row in csv_reader:
                        print("{} {}".format(row[0], row[1]))
                        # print(row)

print_users()

# Solution using DictReader
# def print_users():
#     with open("users.csv") as csvfile:
#         csv_reader = csv.DictReader(csvfile)
#         for row in csv_reader: 
#             print("{} {}".format(row['First Name'], row['Last Name']))