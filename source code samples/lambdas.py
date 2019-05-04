#https://www.python-course.eu/python3_lambda.php

from functools import reduce

sum = lambda x, y: x+y
print (sum (2,4))

#reduce
#Determining the maximum of a list of numerical values by using reduce
g = lambda a,b: a if (a > b) else b
g = reduce( g,[47,11,42,102,13])
print (g)
#Calculating the sum of the numbers from 1 to 100
f = reduce (lambda x,y: x+y, range(1,101))
print (f)