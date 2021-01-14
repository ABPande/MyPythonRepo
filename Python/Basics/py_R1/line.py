class Point():
	x = 0 
	y = 0
	def __init__ (self, x,y):
		self.x = x
		self.y = y
	def getx(self):
		return self.x
	def gety(self):
		return self.y

class Line():
	point = ['','']
	def __init__ (self, point1, point2):
		i=0
		while i < 2:
			x = input("enter x coordinate")			
			if x.isnumeric():
				x = int(x)
				y = input("enter y coordinate")
				if y.isnumeric():
					y = int(y)	
					self.point[i] = Point(x, y)
					i = i + 1
				else:
					print("need better input")
			else:
				print("need better input")
	def __str__ (self):
		return {f"Line from {self.point[0].getx()}, {self.point[0].gety()} to {self.point[1].getx()}, {self.point[1].gety()}"}
	def slope(self):
		return round(((self.point[1].gety() - self.point[0].gety())/(self.point[1].getx() - self.point[0].getx())),2)
	def distance(self):
		return round(((self.point[1].gety() - self.point[0].gety())**2 + (self.point[1].getx() - self.point[0].getx())**2)** 0.5,2)

point1 = Point (3,4)
point2 = Point (9,6)
line1 = Line (point1,point2)
print(line1.distance())
print(line1.slope())

class Cylinder():
	height = 0 
	radius = 0
	pi = 3.14
	def __init__ (self, height, radius):
		self.height = height
		self.radius = radius

	def getVol(self):
		if self.height>0 and self.radius>0:
			return round((self.pi*self.height*(self.radius**2)),2)

	def getSurfaceArea(self):
		if self.height>0 and self.radius>0:
			return round((2*self.pi*self.radius*self.height),2)

h="X"
r="X"

while (not h.isnumeric()):
	h = input ("enter height of a cylinder")
	if h.isnumeric() and int(h)>0:
		h = int(h)
		break
	else:
		print ("numeric and greater than 0 please")
		h=""
if (h > 0):
	while (not r.isnumeric()):
		r = input ("enter radius of a cylinder")
		if r.isnumeric() and int(r)>0:
			r = int(r)
			break
		else:
			print ("numeric and greater than 0 please")
			r=""
	if (r > 0):
		cyl = Cylinder (h,r)
		print(cyl.getVol())
		print(cyl.getSurfaceArea())