import re
# quantity unit collector
# v1 - create layout, try out number regex
# works correctly (for 1 digit only-numbers) as of @25/5/22

# functions needed

# float checker function
def float_checker(question):
    error = "This is not a valid number."
    valid = False
    while not valid:
        # ask user for number and check if it is valid
        try:
            response = float(input(question))
            return response

        # if an integer is not entered, display an error
        except ValueError:
            print(error)
# string checker function
def string_checker(question):

    valid = False
    while not valid:

        response = input(question).title().strip()

        if response != "":
            return response
            break

        else:
            print("Sorry that is not a valid response.")
            print()

# main routine
# because I am not testing ingredient name, it is already set to save time
ingredient_name = "Honey"

quantity = string_checker("What quantity of {} do you need?".format(ingredient_name))

# regular expression to find if item starts with a number
number_regex = "^[1-9]"

# if item has a number, separate it into two (number / item)
if re.match(number_regex, quantity):
    amount = int(quantity[0])
    unit = quantity[1:]
else:
    amount = 1
    unit = quantity

# print for testing purposes
print("You need {} {}".format(amount, unit))
