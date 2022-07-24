import re


# quantity unit collector
# v1 - create layout, try out number regex
# v2 - number regex is working (using re.split) but very breakable
# v3 - added in a while loop to ensure no empty list items
# v4 - put code into function
# v5 - made error prevention for entering a valid unit
# v6 - put the code for inputting the quantity in its own function, that way it
# can be called to other functions for error prevention as necessary - about making
# the code more concise, also added the comprehensive special character for number regex.
# found error, if user re-entered a different amount after unit error prevention,
# the program still takes the first amount. fixing this in next version
# as this code (v6) still mainly works, and I don't want to break it
# v7 - fixing my error prevention for unit (see above), and reorganising code to be more logical
# also added in ml and litres to my list as I realised they are pretty common! plus added more specific error message
# for if user enters a fraction with decimals
# works correctly as of 21/7/22

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


# main routine
# because I am not testing ingredient name, it is already set to save time
ingredient_name = "Honey"

# set quantity question
ask_quantity = ("What quantity of {} can you buy at the store?".format(ingredient_name))

# call quantity function
list_for_quantity = quantity_unit(ask_quantity, ingredient_name)
amount = list_for_quantity[0].strip()
unit = list_for_quantity[1].strip()

# print for testing purposes
print("You need {} {}".format(amount, unit))
