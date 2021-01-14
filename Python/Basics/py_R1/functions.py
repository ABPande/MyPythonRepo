def lessOfTwoEvens (a,b):
	if (a%2==0 and b%2==0):
		if (a>b):
			return b
		return a
	if (a%2!=0 or b%2!=0):
		if (a>b):
			return a
		return b

print (lessOfTwoEvens(2,4))
print (lessOfTwoEvens(3,4))
print (lessOfTwoEvens(3,5))
print (lessOfTwoEvens(5,3))
print (lessOfTwoEvens(6,4))
print (lessOfTwoEvens(4,3))


def animalCrackers(a):
	return (a.split()[0][0].lower()==a.split()[1][0].lower())

print (animalCrackers("Chinese Checkers"))
print (animalCrackers("Australian Kangaroos"))

def makeTwenty (a,b):
	return (((a+b)>=20) or (a==20 or b==20))

print(makeTwenty(12,8))
print(makeTwenty(20,10))
print(makeTwenty(12,7))

def firstAndFourth(name):
	return("".join(name[0].upper()+name[1:3]+name[3].upper()+name[4:]))

print (firstAndFourth("abhijit"))

def reverseString1(strToReverse):
	splitList = strToReverse.split()
	return " ".join([splitList[len(splitList)-x-1] for x in range(0,len(splitList))])

def reverseString2(strToReverse):
	splitList = strToReverse.split()
	return " ".join(splitList[::-1])

print (reverseString1("abhijit goes to office"))
print (reverseString2("abhijit goes to office"))

def within100or200(num):
	return (abs(num - 100) <= 10 or abs(num - 200) <= 10)

print (within100or200(211))

def find33(list33):
	newList = [str(x) for x in list33]
	return ("3_3" in "_".join(newList))

print (find33([1,3,3]))
print (find33([1,3,1,3]))
print (find33([3,3,1,2]))
print (find33([3,2,13,33,1]))

def paperDoll(givenString):
	return "".join([x+x+x for x in list(givenString)])

print (paperDoll("Missisippi"))

def blackJack(a,b,c):
	sumBlackJack = a+b+c
	if (sumBlackJack <= 21):
		return sumBlackJack
	else:
		if (a==11 or b==11 or c==11):
			sumBlackJack = sumBlackJack - 10
			if (sumBlackJack <=21):
				return	sumBlackJack
	return "BUST"

print (blackJack(10,10,10))
print (blackJack(1,1,1))
print (blackJack(11,11,8))
print (blackJack(11,11,11))
print (blackJack(5,5,7))

def summerOf69(arr):
	sum = 0
	i=0
	while i < len(arr):
		if arr[i]!=6:
			sum = sum + arr[i] 
		else:
			while arr[i] != 9 and i < len(arr):
				i = i + 1
		i=i+1
		print(f"i is {i}")
	return sum

print (summerOf69([1,3,5]))
print (summerOf69([4,5,6,7,8,9]))
print (summerOf69([2,1,6,9,11]))

def check007(list007):
	index7=-1
	index0_1=-1
	index0_2=-1
	i = -1
	for var in list007:
		i = i + 1
		if var == 0 and index0_1 == -1:
			index0_1 = i
			continue
		if var == 0 and index0_1 > -1:
			index0_2 = i
			continue
		if var == 7 and index0_1 > -1 and index0_2 > -1:
			index7 = i
			return True
	return False
	
print (check007([1,2,4,0,0,7,5]))
print (check007([1,0,2,4,0,5,7]))
print (check007([1,7,2,0,4,5,0]))

def findPrimes (num):
	prime = False
	primes = [1]
	for i in range(2,num):
		for j in range(2, int(num/2)):
			if i!=j:
				if i%j==0:
					prime = False
					break
				else:
					prime = True
		if prime:
			print(f"{i} is prime")
			primes.append(i)
		else:
			print (f"{i} is not prime")
	return primes 
print (findPrimes(37))

