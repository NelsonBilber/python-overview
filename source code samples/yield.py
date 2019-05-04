
import random

def add(a, b):
    return a + b

def simple_generator_function(): 
    yield 1
    yield "w"
    yield 3 # yield saves last state of iterator

our_generator = simple_generator_function()
print (next (our_generator))
print (add(5,9))
print (next (our_generator))
print (next (our_generator))
#print (next (our_generator)) # no more files to show commands

def netxSquare():
    i = 1
    while True:
        yield i*i
        i += 1

for num in netxSquare():
    if num > 10:
        break
    print (num)

