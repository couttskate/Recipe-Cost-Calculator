import re


# quantity unit collector
# v1 - create layout, try out number regex
# v2 - number regex is working (using re.split) but very breakable
# v3 - added in a while loop to ensure no empty list items
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


# main routine
# because I am not testing ingredient name, it is already set to save time
ingredient_name = "Honey"

# calling string checker to make sure no empty strings are entered
quantity = string_checker("What quantity of {} do you need?".format(ingredient_name))

# using a regular expression to split the string into two after the first alphabet letter
quantity_list = re.split('(\d+)', quantity)

# while there is an empty item in the list, delete it
while ("" in quantity_list):
    quantity_list.remove("")

while len(quantity_list) < 2:
    print("Sorry, you didn’t include both the amount and the unit. Please try again.")
    print()
    quantity = string_checker("What quantity of {} do you need?".format(ingredient_name))
    quantity_list = re.split('(\d+)', quantity)
    while "" in quantity_list:
        quantity_list.remove("")

amount = quantity_list[0]
unit = quantity_list[1]

# print for testing purposes
print("You need {} {}".format(amount, unit))
