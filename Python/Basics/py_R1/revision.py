dict1 = {'key1':"v1",'key2':"v2",'key3':"v3"}
print (dict1)
newKey = "key4"
print (f"{newKey} is being added to dict1")
dict1[newKey] = "v4"
print (dict1)
list1 = ["v5","v6"]
for key,value in dict1.items():
	print (f"key is {key}, value is {value}")
	if (key > "key2"):
		print (f"\t{key} is greater than key2, its value is {value}")
		list1.append(value)
		print (f"\t\tlist 1 is increased, new list1 is {list1}")

print("time to remove objects from a list")
print(list1.pop() + " has been removed")
print (f"new list is {list1}")
list2 = [x for x in range(0,1000) if x%7==0]
#print (list2)
print ("time to play with strings")
string1 = input ("enter a string")
string2 = input ("enter another string")
print (f"string1 is {string1} and string2 is {string2}")
string3 = string1+ string2
list3 = list(string3)
print (list3)
list4 = [list3[x] for x in range(0,len(list3)) if x%2==0]
list5 = [list3[x] for x in range(0,len(list3)) if x%2!=0]
print (list4) 
print (list5)
print("".join(list4) + "".join(list5))
string3 = input ("enter a string") 
split1 = input ("enter a splitpoint")
splitlen = input ("enter number of characters to cut")
strlen = len(string3)
if ((strlen > int(split1) + int(splitlen)) and (int(split1)>0) and (int(split1)< strlen)):
	print (string3[int(split1):int(split1)+int(splitlen):])
else:
	print("retry")

	