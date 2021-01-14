print("I am going\n on a run")
string = "running"
print("I am going\t on a run")
print (len ("hello\n"))

myString = "Hello World"
#indexing strings
print(myString[0])
print(myString[-1])
print(myString[2:4])
print(myString[2:])
print(myString[2::2])

print(myString[::3])
print('Hello World'[8:9])
#string concatenation
string1 = "Hello"
string2 = "World"
print(string1+" "+string2)
print(string1[1:]+ " "+string2[-2:])
print(string1,string2)

#formatting strings
v="variable"
t= "test"
a = 9.994324324
print (f"{t} is a {v}")
print (f"{a:3.5f}")
print('{t} is a {v}'.format(t="something",v="nothing"))
print('{0}{0}{1}{1}'.format("test", "test1"))


