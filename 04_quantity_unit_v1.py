import re
# quantity unit collector
# v1 - create dictionary and number regex
# works correctly as of @

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
ingredient_name = string_checker("What is your ingredient called? ")
quantity = float_checker("What quantity of {} do you need?".format(ingredient_name))

# regular expression to find if item starts with a number
number_regex = "^[1-9]"

# valid dry units holds list of all dry units
# each item in valid units is a list with
# valid options for each unit <full name, letter code (a-e)
# , and possible abbreviations etc>
valid_dry_units = [
    ["Grams", "G", "a"],
    ["Kilograms", "Kgs", "b"],
    ["Cups", "c"],
    ["Teaspoons", "tsp", "d"],
    ["Tablespoons", "tbsp", "e"],
]

# if item has a number, separate it into two (number / item)
if re.match(number_regex, quantity):
    amount = int(quantity[0])
    unit = quantity[1:]
else:
        amount = 1
        unit = unit

# print for testing purposes
print("You need {}".format(ingredient_needed))
print("At the store you can buy {}".format(ingredient_given))
