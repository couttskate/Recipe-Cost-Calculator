# string checker function
# v1 - create basic string checker
# v2 - has a more specific error message to aid users - this version was
# created much later than the first in my revision.
# works correctly as of 21/7/22

# function goes here
def string_checker(question):

    valid = False
    while not valid:

        response = input(question).title().strip()

        if response != "":
            return response

        else:
            print("Sorry you cannot leave this blank.")
            print()

# *** Main Routine starts here ***
recipe_name = string_checker("What is your recipe called?")
print("Your recipe is: ", recipe_name)
print()
