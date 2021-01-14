def piglatin(keyword):
	if keyword[0].lower() in ["a","e","i","o","u"]:
		return keyword + 'ay'
	else: 
		return keyword[1:] + keyword[0] + 'ay'

def evenOdd(a,b):
	greater = 0 
	lesser = 0
	if a > b:
		greater = a
		lesser = b
	else:
		greater = b
		lesser = a
	if a%2 == 0 and b%2 == 0:
		return min(a,b)
	else:
		return max(a,b)
		
def sameWords (s):
	return s.lower().split()[0][0] == s.lower().split()[1][0]

def checkTwenty(a,b):
	return ((a==20 or b==20) or (a+b == 20))

def MacDonald(nameString):
	return (nameString[0].upper() +
	 nameString[1:3] + 
	 nameString[3].upper() +
	 nameString[4:])

def masterYoda(textString):
	reversedlist = textString.split()
	reversedlist.reverse()
	return (' '.join(reversedlist))

def almostThere(a):
	return(abs(100 - a) <= 10 or abs(200-a)<=10)

def has33(list33):
	list33string = [str(x) for x in list33]
	string33 = ''.join(list33string)
	return ('33' in string33)

def times3(string3):
	return ''.join([x*3 for x in list(string3)])

def blackjack (a,b,c):
	blackjackSum = a+b+c
	if blackjackSum > 21:
		if a == 11 or b == 11 or c == 11:
			blackjackSum = blackjackSum - 10
			if blackjackSum <= 21:
				return str(blackjackSum)
			else:
				return "BUST"
		else:
			return "BUST"
	else:
		return str(blackjackSum)

def summerOf69(list69):
	sum69=0
	ignore = False
	for i in list69:
		if i == 6:
			ignore = True
		if not (ignore):
			sum69 = sum69 + i
		if i == 9:
			ignore = False
	return sum69

def find007(list69):
	search0 = False
	search7 = False
	found007 = False
	for i in list69:
		if i == 7 and search7:
			return True
		elif i == 0 and search0:
			search7 = True
			search0 = False
		elif i == 0:
			search0 = True
	return	False


print (find007([1,2,4,0,0,7,5]))
print (find007([1,0,2,4,0,5,7]))
print (find007([1,7,2,0,4,5,0]))
print (summerOf69([1,3,5]))
print (summerOf69([4,5,6,7,8,9]))
print (summerOf69([2,1,6,9,11]))
print (blackjack(1,2,3))
print (blackjack(10,10,1))
print (blackjack(11,10,3))
print (blackjack(11,11,11))
print (times3("hello"))
print (has33([1,3,1,3]))
print (has33([3,1,3,1]))
print (has33([1,3,3,1]))
print (has33([1,1,3,3]))
print (has33([3,3,1,1]))
print (almostThere(96))
print (almostThere(86))
print (almostThere(196))
print (almostThere(186))
print (almostThere(116))
print (almostThere(106))
print (almostThere(216))
print (almostThere(206))

print (masterYoda("I am home"))
print(piglatin("word"))
print(piglatin("apple"))

print (sameWords("Lying Llama"))
print (sameWords("Raging Llama"))

print	(checkTwenty(10,10))
print	(checkTwenty(20,00))
print	(checkTwenty(0,20))
print	(checkTwenty(9,9))
print	(checkTwenty(-1,20))
print	(checkTwenty(20,-1))
print (MacDonald ("abhijit"))
print (str(ord("A")) + " " + str(ord("a")))