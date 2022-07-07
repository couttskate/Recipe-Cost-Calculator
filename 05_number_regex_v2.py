# code adapted from "finxter.com"
# Method 1: re.split()
import re
quantity = '1.11grams'
# regex special character from "regexp.info"
res = re.split('[-+]?([0-9]*\.[0-9]+|[0-9]+)', quantity)
print(res)
res.remove(res[0])
print(res)
