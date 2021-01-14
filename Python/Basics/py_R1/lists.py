def myfunc(strAltCase):
    return "".join("".join([strAltCase[i].upper(),strAltCase[i+1].lower()]) for i in (range(0, len(strAltCase),2)))
print(myfunc ("supernatural"))
my_list = [1,2,3]
print(my_list[1])
my_list = my_list + ['STRING',100]
print (my_list)
my_list[3] = my_list[3].lower()
print(my_list)
my_list.append(1)
print(my_list)
my_list.pop(-4)
print(my_list)

num_list = [4,5,3,4,1,5,3,6,3,4]
num_list.sort()
print (num_list)
print(num_list.index(3))
for i in num_list:
	if i < 4:
		print(i)
new_list = [x+y for x in range(0,50) for y in range(0,2) if x%3==0 ]
print (new_list)
new_list = [x[0] for x in ("Hallejullah Check the first words".split(" "))]
print (new_list)

print ("lists here")
list1 = [1,2,3,4,5,6,7,8,9]
list2= list1[1:9:2]
print (list2)
list1 = ["Abhijit", "abhijit"]
print("_".join(list1).swapcase().split("_"))