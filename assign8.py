#Clears & defines list and dictionary
namenum = {}
lookup = ()

#Defines function to lookup names and numbers
def lookupExtensions(namenum, lookup):
#Compares key to lookup values, if any of them are the same, prints the result as a string
	res = [val for key, val in namenum.items() if lookup in key]
	print(str(res))