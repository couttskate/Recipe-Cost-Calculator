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
ingredient_info = []
while ingredient_name != "xxx":
    ingredient_name = string_checker("What is your ingredient called? ")
    if ingredient_name == "Xxx":
        break
    else:
        ingredient_info.append(ingredient_name)
        ingredient_needed = float_checker("What quantity of {} do you need?".format(ingredient_name))
        ingredient_info.append(ingredient_needed)
        ingredient_given = float_checker("What is the closest quantity you can buy {} at the store?".format(ingredient_name))
        ingredient_info.append(ingredient_given)
        grocery_price = float_checker("What is the price of {} at the store?".format(ingredient_name))
        ingredient_info.append(grocery_price)

print(ingredient_info)


