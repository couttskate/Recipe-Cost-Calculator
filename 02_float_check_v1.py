# float checker function
# v1 - checks that user input is a valid float
# works correctly as of @20/6/22
# function goes here
def float_check(question):
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

# main routine goes here
# get serving size
serving_size = float_check("Please enter the serving size for this recipe: ")




