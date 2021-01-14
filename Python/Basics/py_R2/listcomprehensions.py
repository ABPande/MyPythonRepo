list1 = [ "Sunday" if x % 7 == 0 else "Weekday" for x in range(1,365)]
list2 = [x if x % 3 == 0 else "not multiple" for x in range (0,99+2) if x % 2 == 0]
print(list1)