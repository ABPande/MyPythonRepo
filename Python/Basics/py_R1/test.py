import random
print(random.randint (1,52))
l1 = [1,2]
l2 = [3,4]
l1.append(l2)
print (l1)
print (list(range(1,53)))
l1 = [[x,int((x-1)/13)+1,False,x] for x in range(1,53)]
for item in l1:
	modRes = item[0]%13
	if modRes >= 2 and modRes <=10:
		item[3] = modRes
	if modRes == 1:
		item[3] = 11
	if (modRes > 10 and modRes <= 13) or (modRes == 0):
		item[3] = 10
print (l1)