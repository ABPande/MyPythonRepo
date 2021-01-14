class line():
	def __init__(self, point1, point2):
		self.x1 = point1[0]
		self.y1 = point1[1]
		self.x2 = point2[0]
		self.y2 = point2[1]
	def getSlope(self):
		if self.x2 - self.x1 != 0:
			return (self.y2 - self.y1) / (self.x2 - self.x1)
		else:
			return 0
	def getDistance(self):
		return (((self.x2 - self.x1) ** 2) + ((self.y2 - self.y1) ** 2))**0.5

point1string = input("provide the point x,y values with commas")
line1 = line((3,4),(8,11))
print(line1.getDistance())
print(line1.getSlope())
