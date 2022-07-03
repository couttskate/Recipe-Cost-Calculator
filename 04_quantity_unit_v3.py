import re
# quantity unit collector
# v1 - create dictionary and layout, try out number regex
# v2 - number regex is working (using re.split) but very breakable
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
# because I am not testing ingredient name, it is already set to save time
ingredient_name = "Honey"

# calling string checker to make sure no empty strings are entered
quantity = string_checker("What quantity of {} do you need?".format(ingredient_name))

# using a regular expression to split the string into two after the first alphabet letter
res = re.split('(\d+)', quantity)
res.remove(res[0])
print(res)
amount = res[0]
unit = res[1]

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


# print for testing purposes
print("You need {} {}".format(amount, unit))
