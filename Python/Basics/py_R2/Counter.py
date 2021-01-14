from collections import Counter
list1 = [1,1,2,3,4,5,1,1,2,3,1,2,3,5,6,7,2,2,1,1,2,4,6,7,8]
print(Counter(list1))
print (Counter ('abhijit Pande'))
c = Counter (list1)
print(c.most_common(1))
from collections import defaultdict
d1 = {'k1':1}
print(d1['k1'])
d2 = defaultdict (object)
print(d2['k1'])
print(d2['k2'])
for item in d2:
	print(item)

from collections import OrderedDict

d = {'a':5,'b':4,'c':2,'d':3,'e':1} 
print(d)
for item in sorted(d.values()):
	print (item)

from collections import namedtuple
Dog = namedtuple('Dog','legs spots breed name')
tommy = Dog (4,True, "doberman", "Tommy")
print(tommy[0])
import datetime
t = datetime.time(5,25,1)
print(t)
t = datetime.date(2009,3,31)
print(t)
t = datetime.date.today()
print (t)
t = datetime.datetime.now()
print (t)

import timeit


print(timeit.timeit	('"-".join(str(n) for n in range(1,99))',number = 100000))
print(timeit.timeit	('"-".join([str(n) for n in range(1,99)])',number = 100000))
print(timeit.timeit	('"-".join(map(str,range(1,99)))',number = 100000))