import re

f = open('regex_sum_35735.txt', 'r')
file = f.read()

nums = re.findall(r'\d+', file)

intnums = []
for x in nums:
	number = int(x)
	intnums.append(number)

total = 0

for x in intnums:
	total = total + x

print (total)
return total