if 5>7:
	print ("hello")
elif 7>5:
	print ("Hi")

h = {'k1':1,'k2':3, 'k3':5}
for i in h.values():
	print(i)

i=0
while i in range(0,10):
	i = i + 1
	if i % 2 == 0:
		print(i)	

name = 'Abhijit'

for i in list(name):
	print (i)

for key,value in h.items():
	if key > "k2":
		print (value)
	else:
		print ("smaller than k2")

		