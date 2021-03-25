# The function add_user takes in a first name and a last name and appends this information as a new user to the file users.csv

# Import DictReader
from csv import DictReader, DictWriter, reader, writer

# Solution using DictWriter
# define the function
def add_user(first_name, last_name):
        # Open the CSV file in append mode
        with open("users.csv", "a") as my_file:

                # Note that although the headers row must be defined in order assign it to fieldnames, we will not be writing the header since the header already exists in the file
                headers = ["First Name", "Last Name"]
                csv_writer = DictWriter(my_file, fieldnames=headers)
                csv_writer.writerow({
                        "First Name": first_name,
                        "Last Name": last_name
                })

# Solution using writer
# def add_user(first_name, last_name):
#         # Open the CSV file in append mode
#         with open("users.csv", "a") as my_file:
#                 csv_writer = writer(my_file)
#                 csv_writer.writerow([
#                         first_name,
#                         last_name
#                 ])

add_user("Ryan", "Gosling")

        