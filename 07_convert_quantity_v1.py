import re


# converting quantities component - users might enter any amount or unit for their quantity,
# but for the RCC it will be easier if every ingredient quantity is decimals and grams

# v1 - set up amount conversions using an of if/else statement (in a function)
# works correctly as of 22/7/22

# functions needed


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

        else:
            print("Sorry you cannot leave this blank.")
            print()


# valid unit checker function
def valid_unit(check_list, quantity_question, test_ingredient):
    entered_unit = check_list[1].strip()
    # list of valid measurement units
    valid_units = [
        ["grams", "Grams", "Gram", "G"],
        ["cups", "Cups", "Cup"],
        ["teaspoons", "Tsp", "Teaspoons", "Teaspoon"],
        ["tablespoons", "Tbsp", "Tablespoon"],
        ["eggs", "Eggs", "Egg"],
        ["kgs", "kg", "kilograms", "Kilograms", "Kgs", "Kg", "Kilogram", "kilogram"],
        ["mL", "ML", "Ml", "mLs", "Mls", "millilitre", "Millilitre", "Millilitres", "millilitres"],
        ["L", "l", "litre", "Litre", "litres", "Litres", "Ls"]
    ]

    key_to_lookup = entered_unit
    # initial test to see if unit is in valid list
    for i in valid_units:
        # if unit is registered, return it and break
        if key_to_lookup in i:
            return check_list

    # check that no invalid fraction is entered (a fraction with decimals) as this is beyond the processing
    # capabilities of my program
    while "." in key_to_lookup or "/" in key_to_lookup:
        print("Sorry, you cannot enter fractions with decimal numbers. Please try again.")
        print()
        check_list = quantity_unit(quantity_question, test_ingredient)
        key_to_lookup = check_list[1].strip()

    while key_to_lookup not in valid_units:
        print("The unit you have used is not registered with this program, try again.")
        print()
        check_list = quantity_unit(quantity_question, test_ingredient)
        key_to_lookup = check_list[1].strip()
        for i in valid_units:
            if key_to_lookup in i:
                return check_list


# amount and unit function
def quantity_unit(question, ingredient):
    returning_list_quantities = []
    # calling string checker to make sure no empty strings are entered
    quantity = string_checker(question)

    # using a regular expression to split the string into two after the first alphabet letter
    quantity_list = re.split('[-+]?([0-9]*[\x2f\x2e]*[0-9]+|[0-9]+)', quantity)

    # while there is an empty item in the list, delete it
    while "" in quantity_list:
        quantity_list.remove("")

    # while there are less than 2 items in list, ask for unit and amount again
    while len(quantity_list) < 2:
        print("Sorry, you did not include both the amount and the unit. Please try again.")
        print()
        quantity = string_checker("What quantity of {} do you need?".format(ingredient))
        # using a regular expression to split user input list items,
        # splitting after the first non-digit character
        quantity_list = re.split('[-+]?([0-9]*[\x2f\x2e]*[0-9]+|[0-9]+)', quantity)
        # remove empty items from list again to make sure the loop will exit with correct answer
        while "" in quantity_list:
            quantity_list.remove("")

    # check unit is ok using unit checker, if unit is not registered the program will ask for
    # amount and unit again
    returning_list_quantities = valid_unit(quantity_list, ask_quantity, ingredient_name)
    return returning_list_quantities


# amount conversion function
def convert_amount(converting_amount):
    converted_amount = converting_amount
    # if the amount is a fraction...
    if "/" in converting_amount:
        # split the string into the numerator and denominator
        fraction_list = converting_amount.split("/")
        numerator = fraction_list[0]
        denominator = fraction_list[1]
        # change both strings into integers that can be divided
        numerator = int(numerator)
        denominator = int(denominator)
        # divide numerator by denominator to find decimal equivalent
        converted_amount = numerator / denominator
        # return the decimal amount
        return converted_amount
    # if the amount is already a decimal, return
    elif float(converting_amount):
        return converted_amount
    # if the amount is an integer, convert to float
    else:
        converted_amount = float(converting_amount)
        return converted_amount


# main routine
# because I am not testing ingredient name, it is already set to save time
ingredient_name = "Honey"

# set quantity question
ask_quantity = ("What quantity of {} can you buy at the store?".format(ingredient_name))

# call quantity function
list_for_quantity = quantity_unit(ask_quantity, ingredient_name)
amount = list_for_quantity[0].strip()
unit = list_for_quantity[1].strip()

# call converting amount function to convert all numbers to floats
float_amount = convert_amount(amount)

# print for testing purposes
print("You need {} {}".format(float_amount, unit))
