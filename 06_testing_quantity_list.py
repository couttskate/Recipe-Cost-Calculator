# testing different ways to get rid of empty items in a list

# already set list (for testing purposes)
quantity_list = ["", "123", "", ""]
# 1st way - using a for loop
for x in quantity_list:
    # if the item is empty
    if x == "":
        # delete it
        quantity_list.remove(x)

print(quantity_list)

# 2nd way - using a while loop
# while there is an empty item in the list, delete it
while("" in quantity_list):
    quantity_list.remove("")

print(quantity_list)
