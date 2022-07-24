import re

# recipe cost calculator program - base

# v1 - outlining where components will go, adding string and float checker and basic welcome info
# v2 - originally adding ingredient info component however this has been rethought as it was too difficult
# v3 - adding in all the components that gather ingredient info (the valid unit component, quantity unit component +
# the converting quantity component)
# I can insert these components into the slot where my original 'ingredient info component' would have gone
# also updated my string checker to version 2.

# functions go here


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
        ["kgs", "kg", "kilograms", "Kilograms", "Kgs", "Kg"],
        ["mL", "ML", "Ml", "mLs", "Mls", "millilitre", "Millilitre", "Millilitres", "millilitres"],
        ["L", "l", "litre", "Litre", "litres", "Litres"]
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


# converting amount to float function
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
        print(converting_amount)
        return converted_amount


# converting all units to grams and finding equivalent amount function
def convert_unit(converted_amount, converting_unit):
    # lists of valid measurement units
    grams = ["grams", "Grams", "Gram", "G"]
    cups = ["cups", "Cups", "Cup"]
    tsp = ["teaspoons", "Tsp", "Teaspoons", "Teaspoon"]
    tbsp = ["tablespoons", "Tbsp", "Tablespoon"]
    eggs = ["eggs", "Eggs", "Egg"]
    kg = ["kgs", "kg", "kilograms", "Kilograms", "Kgs", "Kg", "Kilogram", "kilogram"]
    ml = ["mL", "ML", "Ml", "mLs", "Mls", "millilitre", "Millilitre", "Millilitres", "millilitres"]
    l = ["L", "l", "litre", "Litre", "litres", "Litres", "Ls"]

    # if the quantity is entered in kilograms or litres
    if converting_unit in kg or converting_unit in l:
        # converting to float to ensure number not treated as string, doing this for each if
        # statement to prevent errors
        float_num = float(converted_amount)
        # a litre of water is equal to 1 kilogram or 1000 grams
        to_make_same = 1000
        gram_amount = (to_make_same * float_num)
        return gram_amount
    # if the quantity is entered in cups
    if converting_unit in cups:
        float_num = float(converted_amount)
        # 1 cup of water is 240 grams
        to_make_same = 240
        gram_amount = (to_make_same * float_num)
        return gram_amount
    # if the quantity is entered in teaspoons
    if converting_unit in tsp:
        float_num = float(converted_amount)
        # 1 tsp of water is 5 grams
        to_make_same = 5
        gram_amount = (to_make_same * float_num)
        return gram_amount
    # if the quantity is entered in tablespoons
    if converting_unit in tbsp:
        float_num = float(converted_amount)
        # 1 tbsp of water is 15 grams
        to_make_same = 15
        gram_amount = (to_make_same * float_num)
        return gram_amount
    # if the quantity is entered in litres
    if converting_unit in eggs:
        float_num = float(converted_amount)
        # 1 egg is 60 grams
        to_make_same = 60
        gram_amount = (to_make_same * float_num)
        return gram_amount
    # if the quantity is entered in grams or millilitres, keep amount the same and return
    # (1 millilitre of water is equal to 1 gram)
    if converting_unit in grams or converting_unit in ml:
        return converted_amount

# main program

# lists go here (used mainly for pandas)

# list for ingredients used
# list for quantity needed in recipe
# list for quantity given
# list for price of quantity given
# list for total price of the whole recipe


# welcome info
print("Welcome To Kate's Recipe Calculator!")
print()
print()
print("This program will calculate how much your recipe costs, and how much it will cost per serve.")
print()
print()

# call string checker for recipe name
recipe_name = string_checker("What is your recipe called?")

# call float checker for serving size
serving_size = float_checker("Please enter the serving size for this recipe: ")

# repeat info (for testing purposes)
print("Your recipe is: ", recipe_name)
print("Your serving size is:", serving_size)

# while loop for ingredients
ingredient_name = ""
ingredient_info = []
while ingredient_name != "xxx":
    ingredient_name = string_checker("What is your ingredient called? ")
    if ingredient_name == "Xxx":
        break
    else:
        # set quantity question ( ask what quantity of their ingredient they can buy at the store )
        ask_quantity = ("What quantity of {} can you buy at the store?".format(ingredient_name))

        # call quantity function
        list_for_quantity = quantity_unit(ask_quantity, ingredient_name)
        amount = list_for_quantity[0].strip()
        unit = list_for_quantity[1].strip()

        # call converting amount function to convert all numbers to floats
        float_amount = convert_amount(amount)

        # call converting amount function to convert all numbers to their gram equivalent
        store_quantity = convert_unit(float_amount, unit)

        # print for testing purposes
        print("You can buy {} grams at the store.".format(store_quantity))

        # ask how much this amount costs
        store_price = float_checker("How much does this cost: $")

        # ask what quantity of their ingredient the recipe requires
        ask_quantity = ("What quantity of {} does your recipe require?".format(ingredient_name))

        # call quantity function
        list_for_quantity = quantity_unit(ask_quantity, ingredient_name)
        amount = list_for_quantity[0].strip()
        unit = list_for_quantity[1].strip()

        # call converting amount function to convert all numbers to floats
        float_amount = convert_amount(amount)

        # call converting amount function to convert all numbers to their gram equivalent
        recipe_quantity = convert_unit(float_amount, unit)

        # print for testing purposes
        print("Your recipe needs {} grams.".format(recipe_quantity))





print(ingredient_info)

# calculating total and per serve price

# print all
