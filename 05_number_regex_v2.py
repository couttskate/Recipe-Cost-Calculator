# code adapted from "finxter.com"
# Method 1: re.split()
import re
quantity = '1.11grams'
# regex special character from "regexp.info"

# this regular expression matches an optional
# sign, that is either followed by zero or more
# digits followed by a dot and one or more digits
# (a floating point number with optional integer part),
# or that is followed by one or more digits (an integer)
res = re.split('[-+]?([0-9]*\.[0-9]+|[0-9]+)', quantity)
print(res)
res.remove(res[0])
print(res)
