
# code to check how to find an item within a list within a list

dict1 = [["grams","g","G","GRAMS","Grams"], ["tablespoons","TBS","tbs","Tablespoons", "TABLESPOONS"]]

key_to_lookup = "g"
break_out = ""
for i in dict1:
    if break_out == "quit":
        break
    print(i)
    for j in i:
        print(j)
        if key_to_lookup in i:
            print("true")
            break_out = "quit"
            break
        else:
            print("false")

x = 1.0 * 1/2
print(x)
