import re


# quantity unit collector
# v1 - create layout, try out number regex
# v2 - number regex is working (using re.split) but very breakable
# v3 - added in a while loop to ensure no empty list items
# v4 - put code into function
# v5 - made error prevention for entering a valid unit
# v6 - put the code for inputting the quantity in its own function, that way it
# can be called to other functions for error prevention as necessary - about making
# the code more concise.
# works correctly as of @8/7/22

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


# amount and unit function
def quantity_unit(question, ingredient):
    # calling string checker to make sure no empty strings are entered
    quantity = string_checker(question)

    # using a regular expression to split the string into two after the first alphabet letter
    quantity_list = re.split('(\d+)', quantity)

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
        quantity_list = re.split('(\d+)', quantity)
        # remove empty items from list again to make sure the loop will exit with correct answer
        while "" in quantity_list:
            quantity_list.remove("")
    return quantity_list


# valid unit checker function
def valid_unit(entered_unit, quantity_question, test_ingredient):
    # list of valid measurement units
    valid_units = [
        ["grams", "Grams", "Gram", "G"],
        ["cups", "Cups", "Cup"],
        ["teaspoons", "Tsp", "Teaspoons", "Teaspoon"],
        ["tablespoons", "Tbsp", "Tablespoon"],
        ["eggs", "Eggs", "Egg"],
        ["kilograms", "Kilograms", "Kgs"]
    ]

    key_to_lookup = entered_unit
    accept_unit = False
    # initial test to see if unit is in valid list
    for i in valid_units:
        # if unit is registered, return it and break
        if key_to_lookup in i:
            accept_unit = True

    while not accept_unit:
        key_to_lookup = entered_unit
        for i in valid_units:
            if key_to_lookup in i:
                print("yay")
                break
        print("The unit you have used is not registered with this program, try again.")
        print()
        try_again = quantity_unit(quantity_question, test_ingredient)
        entered_unit = try_again[1].strip()

    return entered_unit


# main routine
# because I am not testing ingredient name, it is already set to save time
ingredient_name = "Honey"

# set quantity question
ask_quantity = ("What quantity of {} can you buy at the store?".format(ingredient_name))

# call quantity function
list_for_quantity = quantity_unit(ask_quantity, ingredient_name)
amount = list_for_quantity[0].strip()
unit = list_for_quantity[1].strip()
print(list_for_quantity, amount, unit)

# check unit is ok
valid_unit(unit, ask_quantity, ingredient_name)
# print for testing purposes
print("You need {} {}".format(amount, unit))
