import re

patterns = ['term1','term2']
text = "this is a string with term1"
text1 = "here is a text which has two term1, one before this and one here - term1" 

for num, pattern in enumerate(patterns):
	print ("\nsearching... pass" + str(num))
	matchobject = re.search(pattern,text)
	matchobject2 = re.findall(pattern, text1)
	if matchobject:
		print("match found in text")
		print (matchobject.start())
		print (matchobject.end())
	else:
		print("not found in text")
	if len(matchobject2)>0:
		print("match found in text1")
		print (matchobject2)
	else:
		print("not found in text1")
