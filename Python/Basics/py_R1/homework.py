def vol(r):
	return round((4/3)*3.14*(r**3),2)

print(vol(4))

def rangeCheck(num, high, low):
	return (low<=num<=high)

print (rangeCheck(5,10,3))
print (rangeCheck(7,5,3))

def upperLowerCount(stringToCheck):
	print (len([x for x in list(stringToCheck) if x.isupper()]))
	print (len([x for x in list(stringToCheck) if x.islower()]))

print (upperLowerCount("BlahBlahBlah"))

def uniqueList(firstList):
	return list(set(firstList))

print (uniqueList([1,1,1,2,2,2,3,3,3,4,4,5,5,6,7]))

def multiplyAll(*args):
	prod = 1
	for var in args:
		prod = prod*var
	return prod

print (multiplyAll(1,2,3,4,5,6))

def palindromeCheck(stringToCheck):
	return stringToCheck == stringToCheck[::-1]

print (palindromeCheck ("heehaheeh"))
print (palindromeCheck ("ooof"))

def pangramCheck (stringToCheck):
	list_Alphabet = ("a","b","c","d","e","f","g","h","i",'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
	return set(list_Alphabet)<=set(stringToCheck)

print (pangramCheck("the quick brown fox jumps over the lazy dog"))

