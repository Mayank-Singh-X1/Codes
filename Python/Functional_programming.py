def cube(x):
    return x*x*x

l=[1,3,5,7,9,4]
g=list(map(cube,l))       #map 
print(g)


j=list(filter(lambda x:x%2==0,l))      #filter
print(j)

from functools import reduce
j=reduce(lambda x,y:x+y, l)  #reduce
print(j)