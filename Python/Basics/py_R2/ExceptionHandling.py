global file1 
file1 = None
try:
	file1 = open("ExceptionTest.txt",w)
	file1.write ("Blah blah black sheep\n Have you any wool")
	output = file1.read()
except:
	print("Something went wrong")
else:
	print("here is the content")
	print(output)
finally:
	print("good night")
	file1.close