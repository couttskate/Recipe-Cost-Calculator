import pandas
# ingredient info function
# v1 - ask for ingredient name, quantities and price

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


# main routine

# while loop for ingredients
ingredient_name = ""
while ingredient_name != "xxx":
    ingredient_info = []
    ingredient_name = string_checker("What is your ingredient called? ")
    ingredient_needed = float_checker("What quantity of {} do you need?".format(ingredient_name))
    ingredient_given = float_checker("What is the closest quantity you can buy {} at the store?".format(ingredient_name))
    grocery_price = float_checker("What is the price of {} at the store?".format(ingredient_name))
    new_info = (ingredient_name, ingredient_needed, ingredient_given, grocery_price)
    ingredient_info.extend(new_info)

print(ingredient_info)


