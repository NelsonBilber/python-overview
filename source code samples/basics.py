import sys
from copy import deepcopy
from mymodules import fibonacci #custom modules

# for loop

def forloops():
    name = input ("Name: ")
    i = 0 # acummulator pattern aka counter
    for c in name:
        print (c)
        i = i+1 
    print ("number of characters ", i)   

# list

def usingLists(): 
    activity = "two"
    activities = ["one", "two", "five"]
    if activity in activities:
        print ("find ! ")
    addact = ["ten"]
    activities = activities + addact
    for act in activities:
        print (act)
    addact = ["twenty"]
    for act in activities: # does not change like a C++ pointer
        print (act)

def ReadFromFile():
    infile = open ("input.txt", "r")
    allLine = ""
    for line in infile:
        # print (line)
        sys.stdout.write(line) #print without new line
        allLine = allLine + line
    infile.close()
    WriteFromFile(allLine)

def WriteFromFile(infile):
    outfile = open ("output.txt","w")
    for line in infile:
        outfile.write(line)
    outfile.close

def returnValues(a, b): 
    return a + b # return values

def funcNumVarParams(*args):
    return len(args)

def ShallowAndDeepCopy():
    lst1 = ['blue','red']
    lst2 = lst1
    print (lst1)
    print (lst2)
    print (id(lst1), id(lst2))
    lst2 = ['blue','green']
    print (lst1)
    print (lst2)
    print (id(lst1), id(lst2))
    #use a deepcopy method
    lst3 = deepcopy(lst2)
    print (lst3)
    print (id(lst2), id(lst3))


def ref_demo(x):
    print("x=",x," id=",id(x))
    x=42
    print("x=",x," id=",id(x))
    return x
 
if __name__ == "__main__":
    
    #forloops()
    #usingLists()
    
    #ReadFromFile()
    #WriteFromFile()
    
    print (returnValues(7,8))
    print ("Num. of args: ", funcNumVarParams(2,19,4))
    ShallowAndDeepCopy()
    print ("Fibonacci: ", fibonacci.fib(10))
    
    x = 89
    x = ref_demo(x) # it pass value by copy, we have to assing the value again in order to have the updated value
    print("Value: ", x)