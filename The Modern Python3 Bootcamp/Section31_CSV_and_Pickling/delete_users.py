# In this exercise, the function delete_users() takes in a first name and a last name. It updates the users.csv file so that any user whose first and last names match the input are removed from the file. The function returns the number of users removed

from csv import DictReader, DictWriter

def delete_users(first_name, last_name):
        # Open the file in read mode
        with open("users.csv", 'r') as file:
                # create the csv_reader object
                csv_reader = DictReader(file)

                # Initiate a list that will hold the OrderedDicts that we create as we iterate through each row
                new_user_list = []

                # Initiate a counter for number of updated users. 
                num_users_removed = 0

                # Iterate through each OrderedDict item and check whether the First Name and Last Name keywords match the old_FN and old_LN values given to the function
                for row in csv_reader:
                        
                        # If there is a match, increment the num_users_removed variable by 1 and DO NOT add this user to the new_user_list
                        if row["First Name"] == first_name and row["Last Name"] == last_name:
                                num_users_removed += 1
                        # If there is no match for that row, append the OrderedDict for that row to the new_user_list as we are not removing this user
                        else:
                                new_user_list.append(row)
                # Verification
                print(new_user_list)
        
        # Now open the users.csv file in write mode
        # with open("users2.csv", 'w') as file:
        with open("users.csv", 'w') as file:
                # Define the headers
                headers = ["First Name", "Last Name"]
                # Create the DictWriter object. Newline lineterminator is helpful to ensure lines are not skipped when writing the CSV
                csv_writer = DictWriter(file, fieldnames=headers, lineterminator = '\n')
                # Write the header
                csv_writer.writeheader()

                for user in new_user_list:
                        csv_writer.writerow(user)
        
        # Finally, return the number of users updated
        return "Users deleted: {}.".format(num_users_removed)

print(delete_users("Grace", "Hopper"))
print(delete_users("Colt", "Steele"))
print(delete_users("Not", "Here"))

# Instructor's solution
# def delete_users(first_name, last_name):
#     with open("users.csv") as csvfile:
#         csv_reader = csv.reader(csvfile)
#         rows = list(csv_reader)
 
#     count = 0
#     with open("users.csv", "w") as csvfile:
#         csv_writer = csv.writer(csvfile)
#         for row in rows:
#             if row[0] == first_name and row[1] == last_name:
#                 count += 1
#             else:
#                 csv_writer.writerow(row)
 
#     return "Users deleted: {}.".format(count)