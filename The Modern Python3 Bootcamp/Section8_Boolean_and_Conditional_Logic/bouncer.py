# ask for age

age = input("How old are you? (please use integers): ")

# check to be sure the user entered a value by making sure age is not an empty string. The embedded conditionals that are nested within this check will onyl run if age is not an empty string.
# you could also test whether age is Truthy or Falsy
# we will later learn how to check whether the user enters a string that can be converted to an integer
# if age != "":
#         age = int(age)
#         # Remember to convert the input ages to integers
#         # 18-21 - wristband
#         if age >= 18 and age < 21:
#                 print("You can enter, but need a wristband. You cannot drink!")

#         # 21+, normal entry
#         elif age >= 21:
#                 print("You are good to enter and can drink!")

#         # <18, too young, sorry
#         else:
#                 print("Sorry, you are too young to enter :(")

# else:
#         print("Please enter an age")

# Another approach that is more efficient by getting rid of the and statements

if age != "":
        age = int(age)
        if age >= 21 :
                print("You can enter and can drink!")
        # here, we only need to check if you are older than 18 because we have already check if you are older than 21. The code in this elif block will not run if age is greater than 21.
        elif age >= 18:
                print("You can enter but need a wristband.  You cannot drink!")
        else:
                print("Sorry, you are too young to enter :(")

else:
        print("Please enter an age")