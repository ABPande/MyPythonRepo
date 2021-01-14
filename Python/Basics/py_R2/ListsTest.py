mylist = [1,2,3]
print(mylist)
mylist.append(4)
print(mylist)
print(mylist.pop())
print(mylist)

mylist.reverse()
print(mylist)
newlist = mylist
mylist.reverse()
print(newlist)
print(mylist)
mylist = mylist*3
print(mylist)
mylist = mylist + newlist
print(mylist)
print(mylist[2:3])
print(mylist[4:5])
createlist = list([mylist[2:3][0],mylist[4:5][0]])
print(createlist)

