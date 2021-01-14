with open("C:\\Machine Learning\\Files\\pyfile1.txt", mode="w") as f:
	f.write("1,2,3,4")
	f.close
with open("C:\\Machine Learning\\Files\\pyfile1.txt", mode="a") as f:
	f.write("\n5,6,7,8")
	f.close
with open("C:\\Machine Learning\\Files\\pyfile1.txt", mode="r") as f:
	contents = f.readline()
	mylist = list(contents.replace("\n","").split(","))
	print (mylist)
	for i in mylist:
		j=2
		while j <= (int(i)/2):
			if (int(i) % int(j)) ==0:
				j=int(i) + 4
			else:
				j=j+1
		if j > (int(i) + 3):
			print ("not prime ",i)
		else:
			print ("prime ",int(i))
	f.close
	