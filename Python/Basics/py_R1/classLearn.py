class SampleWord():
	pass

class Dog():
	breed = 'Dog'
	name = "Name"
	spots = False
	def __init__(self, breed, name, spots):
		self.breed = breed
		self.name = name
		self.spots = spots
		print (self.breed, " ", self.name, " ",self.spots)
	def getSpots (self):
		return self.spots
	def getBreed (self):
		return self.breed
	def getName (self):
		return self.name


mysample = SampleWord()
type(mysample) 

myDog = Dog("Alsatian", "Tommy", False)
print (myDog.getName())
print (myDog.getBreed())
print (myDog.getSpots())

