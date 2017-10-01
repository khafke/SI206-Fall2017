import os
import filecmp
import csv
from operator import itemgetter

def getData(file):
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	with open(file, 'r') as f:
		reader = csv.reader(f)
		dict = {}
		ls = []
		for x in reader:
			dict['First'] = x[0]
			dict['Last'] = x[1]
			dict['Email'] = x[2]
			dict['Class'] = x[3]
			dict['DOB'] = x[4]
			ls.append(dict.copy())

		return (ls)
		


#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName

	#Your code here:
	
	if col == 'First':
		firstlist = []
		for x in data:
			first = x['First']
			last = x['Last']
			name = (first + ' ' + last)
			firstlist.append(name)
		firstnamesort = sorted(firstlist)
		return firstnamesort[0]

	elif col == 'Last':
		lastlist = []
		lastnamesort = sorted(data, key=itemgetter('Last'))
		for x in lastnamesort:	
			first = x['First']
			last = x['Last']
			name = (first + ' ' + last)
			lastlist.append(name)
		return lastlist[0]

	elif col == 'Email':
		emaillist = []
		emailsort = sorted(data, key=itemgetter('Email'))
		for x in emailsort:	
			first = x['First']
			last = x['Last']
			name = (first + ' ' + last)
			emaillist.append(name)
		return emaillist[0]

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:

	freshman = 0
	sophomore = 0
	junior = 0
	senior = 0
	classnames = ['Senior', 'Junior', 'Sophomore', 'Freshman']
	classcount = []
	for x in data:
		if x['Class'] == 'Senior':
			senior = senior + 1
		if x['Class'] == 'Junior':
			junior = junior + 1
		if x['Class'] == 'Sophomore':
			sophomore = sophomore + 1
		if x['Class'] == 'Freshman':
			freshman = freshman + 1
	classcount.append(senior)
	classcount.append(junior)
	classcount.append(sophomore)
	classcount.append(freshman)
	classandcount = list(zip(classnames, classcount))
	sortedsize = sorted(classandcount, key=lambda x: x[1], reverse=True)
	return sortedsize


# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	
	#Your code here:
	numdays = {}
	for x in a[1:]:
		DOB = x['DOB']
		splitDOB = DOB.split('/')
		day = splitDOB[1]
		if day not in numdays:
			numdays[day] = 1
		else:
			numdays[day] += 1
	
	sorted(numdays.values())
	sorted(numdays, key=numdays.get)
	sorteddays = sorted(numdays.items(), key=lambda x:x[1], reverse = True)
	
	return int(sorteddays[0][0])


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	pass

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	pass



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()


