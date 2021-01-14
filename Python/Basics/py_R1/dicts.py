dict1 ={'key1':"value1",'key2':"value2"}
print (dict1)
print(dict1['key1'])
dict1['key3']="test"
print (dict1)
for i in dict1.values():
	if i >= "value":
		print (i)
	else:
		print ("Key 3 was found")
dict2 = {1:"a",2:"b"}
print (dict2.values())
print (dict2.keys())