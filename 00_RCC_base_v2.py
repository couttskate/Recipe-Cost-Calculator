# recipe cost calculator program
# v1 - outlining where components will go, adding string and float checker and basic welcome info

# functions go here

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

# ingredient info function

# dictionary of measurement units

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
print("Your recipe is: ", recipe_name)

# call float checker for serving size
serving_size = float_checker("Please enter the serving size for this recipe: ")
print("Your serving size is:", serving_size)
# repeat info (for testing purposes)

# while loop for ingredients

# call ingredient info function

# calculating total and per serve price

# print all
