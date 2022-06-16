# string checker function
# v1 - create basic string checker
# works correctly as of 17/6/22

# function goes here
def string_checker(question):

    valid = False
    while not valid:

        response = input(question).title().strip()

        if response != "":
            return response
            break

        else:
            print("sorry that is not a valid response")
            print()

# *** Main Routine starts here ***
recipe_name = string_checker("What is your recipe called?")
print("Your recipe is: ", recipe_name)
print()
