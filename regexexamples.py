#Regular Expressions Why
log = "July 31 07:51:48 deshaonscomputers bad proceess [12345]: Error Performing package upgrade"
index = log.index("[")
print(log[index+1:index+6])

# Result 12345
# ALThis is not good enough so regular expressions is needed

import re
log = "July 31 07:51:48 deshaonscomputers bad proceess [12345]: Error Performing package upgrade"
regex = r"\[(\d+)\]"
result = re.search(regex, log)
print(result[1])

#result 12345
#same as above but better with reg ex.

