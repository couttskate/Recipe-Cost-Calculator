# code adapted from "finxter.com"
# Method 1: re.split()
import re
quantity = '1/11grams'
# regex special character from "regexp.info"

# this regular expression matches integers, floats and fractions
# (using the slash eg 1/4) this means it is very user friendly
# for any type of measurement
res = re.split('[-+]?([0-9]*[\x2f\x2e]*[0-9]+|[0-9]+)', quantity)
print(res)
res.remove(res[0])
print(res)
