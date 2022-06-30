# Method 1: re.split()
import re
quantity = '111grams'
res = re.split('(\d+)', quantity)
print(res)

