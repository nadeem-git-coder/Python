'''a,b,c ='123889'
print(a,b,c)'''
'''
gen = (i**2 for i in range(3))
type(gen)
a,b,c = gen
print(type(gen))
print(a,b,c)'''
from typing import Counter, DefaultDict


'''d={'1':2 , '2':4}

a,b = d.items()'''
#print(a,b)

#a,b = dict((1,2))
#print(a,b)

#[a,b,c]= 1,2,3
#print(a,b,c)

#print(type(range()))  range is a type class
'''x,y,z =range(3)
x,y,z = list(range(3))
print(x,y,z)'''

'''
import collections
print(dir (collections))
print(help(collections.namedtuple))'''

#word='dgfudcgdyfgfygdyw6te6'
#print(Counter(word))
l =[1,1,2,2,2,1,1,5,5,5,2,3,3,4,1]
d ={}

for i in l:
    if i in d:
        d[i].append(i)
    else:
        d[i]=[i]

print(d)

print(2+1)




