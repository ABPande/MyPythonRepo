string2 = input("name please")
string1 = "Hello"
print((string1+" " +string2+" ")*3)
print (string1[::-1] + " "+ string2[1:3:])
l = list(string1 + " "+string2)
count = 0
for item in l:
	if item == " ":
		print(("".join(l)[count+1:]).swapcase())
		break
	else:
		count = count+1
print ("this is a string {b} {a}".format (a="test2",b="test1"))
print (f"{string1}")

