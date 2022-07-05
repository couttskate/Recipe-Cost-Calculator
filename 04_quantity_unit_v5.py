import re


# quantity unit collector
# v1 - create layout, try out number regex
# v2 - number regex is working (using re.split) but very breakable
# v3 - added in a while loop to ensure no empty list items
# v4 - put code into function
# works correctly as of @5/7/22

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


def list_checker (choice,options):
    for var_list in options:

            #if the unit is in one of the lists, return the full
            if choice in var_list:

                #get full name of the unit and put it
                #in title case so it looks nice when outputted
                chosen = var_list[0].title()
                is_valid = "yes"
                break

            # if the chosen unit is not valid, set unit_ok to no
            else:
                is_valid = "no"


# amount and unit function
def quantity_unit(question, ingredient):
    # calling string checker to make sure no empty strings are entered
    quantity = string_checker(question)

    # using a regular expression to split the string into two after the first alphabet letter
    quantity_list = re.split('(\d+)', quantity)

    # while there is an empty item in the list, delete it
    while ("" in quantity_list):
        quantity_list.remove("")

    while len(quantity_list) < 2:
        print("Sorry, you didn’t include both the amount and the unit. Please try again.")
        print()
        quantity = string_checker("What quantity of {} do you need?".format(ingredient))
        quantity_list = re.split('(\d+)', quantity)
        while "" in quantity_list:
            quantity_list.remove("")
    # second item in list is the measurement unit
    unit_q = quantity_list[1]
    print(unit_q)
    # dictionary of valid measurement units
    valid_units = [
      ["grams", "Grams", "Gram", "G"],
      ["cups", "Cups", "Cup"],
      ["teaspoons", "Tsp", "Teaspoons", "Teaspoon"],
      ["tablespoons", "Tbsp", "Tablespoon"],
      ["eggs", "Eggs", "Egg"],
      ["kilograms", "Kilograms", "Kgs"]
    ]
    print(valid_units)

    # checks to see if the unit entered by user is valid
    unit_choice = string_checker(unit_q, valid_units)
    quantity_list.pop()
    quantity_list.append(unit_choice)
    return quantity_list


# main routine
# because I am not testing ingredient name, it is already set to save time
ingredient_name = "Honey"

# call quantity function
quantity_list = quantity_unit("What quantity of {} can you buy at the store?".format(ingredient_name), ingredient_name)
amount = quantity_list[0]
unit = quantity_list[1]

# print for testing purposes
print("You need {} {}".format(amount, unit))
