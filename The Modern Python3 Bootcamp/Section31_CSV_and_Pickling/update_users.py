# In this exercise, the function update_users() takes in an old first name, an old last name, a new first name, and a new last name. It updates the users.csv file so that any user whose first and last names match teh old first and last names are updated to hte new first and last names. The function should return a count of how many users were updated

from csv import DictReader, DictWriter

def update_users(old_FN, old_LN, new_FN, new_LN):
        # Open the file in read mode
        with open("users.csv", 'r') as file:
                # create the csv_reader object
                csv_reader = DictReader(file)

                # Initiate a list that will hold the OrderedDicts that we create as we iterate through each row
                new_user_list = []

                # Initiate a counter for number of updated users. 
                num_users_updated = 0

                # Iterate through each OrderedDict item and check whether the First Name and Last Name keywords match the old_FN and old_LN values given to the function
                for row in csv_reader:
                        
                        # If there is a match, add a new dictionary with the new first and last name to the new_user_list. Then increment the num_users_updated variable by 1
                        if row["First Name"] == old_FN and row["Last Name"] == old_LN:
                                new_user_list.append({
                                        "First Name": new_FN,
                                        "Last Name" : new_LN
                                })
                                num_users_updated += 1
                        # If there is no match for that row, simply append the OrderedDict for that row to the new_user_list
                        else:
                                new_user_list.append(row)
                # Verification
                # print(new_user_list)
        
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
        return "Users updated: {}.".format(num_users_updated)


print(update_users("Grace", "Hopper", "Hello", "World")) # Users updated: 1.
print(update_users("Colt", "Steele", "Boba", "Fett"))# Users updated: 2.
print(update_users("Not", "Here", "Still not", "Here")) # Users updated: 0.

# Instructor's solution: Store the existing data in a list, and simply do the update conditionally when writing

# def update_users(old_first, old_last, new_first, new_last):
#     with open("users.csv") as csvfile:
#         csv_reader = csv.reader(csvfile)
#         rows = list(csv_reader)
 
#     count = 0
#     with open("users.csv", "w") as csvfile:
#         csv_writer = csv.writer(csvfile)
#         for row in rows:
#             if row[0] == old_first and row[1] == old_last:
#                 csv_writer.writerow([new_first, new_last])
#                 count += 1
#             else:
#                 csv_writer.writerow(row)
 
#     return "Users updated: {}.".format(count)