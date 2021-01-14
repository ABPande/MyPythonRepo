print (2**3)
print (f"{0} {2}", (2,3,5) )
print ("{1}{0}".format(2,3))
print ("hello"[1:3])
print ([1,2,3,4])
print ({"a":"blah","b":"blah1"}['a'])
print (7**4)
print ("Hi there sam".split())
print ("dog" in "Hi dog")
earth = "Earth"
diameter = "12472"
print ("The diameter of {a} is {b} kilometers".format(a="Earth",b="12472"))
print (f"The diameter of {earth} is {diameter} kilometers")

def getDomain(emailaddress):
	lstAddress = emailaddress.split("@")
	return lstAddress[len(lstAddress)-1]

print(getDomain ("abhijit.a.pande@gmail.com"))

def countDog (dogString):
	lstDogs = dogString.upper().split()
	lstDogCount = [1 for x in lstDogs if "DOG" in x]
	print	(lstDogCount)
	return(len(lstDogCount))

print (countDog("Dog1 is chasing Dog2"))

def caughtSpeeding(birthday, speed):
	limit = 60
	if birthday:
		limit = limit + 5
	if speed > limit + 20:
		return "big Ticket" 
	elif speed > limit:
		return "small Ticket"
	else:
		return "safe"

print(caughtSpeeding(False,59))
print(caughtSpeeding(False,60))
print(caughtSpeeding(False,61))
print(caughtSpeeding(False,79))
print(caughtSpeeding(False,80))
print(caughtSpeeding(False,81))

print(caughtSpeeding(True,64))
print(caughtSpeeding(True,65))
print(caughtSpeeding(True,66))
print(caughtSpeeding(True,84))
print(caughtSpeeding(True,85))
print(caughtSpeeding(True,86))