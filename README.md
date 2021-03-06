# Python

Many has been written about the increase of usage of python on software development. It's one of the most popular programming languages during last 3 years.

So I decide to give it a try.

My perspective is from *Software Engineer* point of view with background in C++ and C# programming languages.

## Table of Contents
1. [Basics](#id-basics) <br/>
   1.1. [Loops](#id-basics-loops) <br/>
   1.2. [Deep and Shallow Copies](#id-basics-deep)<br/>
   1.3. [Modules](#id-basics-modules)<br/>
   1.4. [lambdas](#id-basics-lambdas)<br/>
   1.5. [Recursion](#id-basics-recursion)<br/>
   1.6. [Copy By Reference or Value](#id-copy)<br>
   1.7. [Instance, Class, and Static Methods](#id-static-class)<br/>
   1.8. [Class or Static Variables in Python](#id-static-vars)<br/>
2. [Not so Basic](#id-not-basic) <br/>
   2.1. [Reflection](#id-basics-reflection)<br/>
   2.2. [hooks](#id-basics-hooks)<br/>
   2.3. [yield](#id-basics-yield)<br/>
3. [Files](#id-files) <br/>
4. [Data Structures](#id-data) <br/>
   4.1. [List Comprehensions](#id-lc) <br/>
5. [Object Oriented](#id-oo) <br/>
   5.1. [Inheritance](#id-oo-inheritance) <br/>
6. [Math](#id-math) <br/>
   6.1. [numpy](#id-numpy) <br/>
7. [Network](#id-network) <br/>
   7.1. [Echo Server](#id-network-echo-server)<br/>
8. [Software Architecture](#id-arch) <br/>
   8.1. [Unit Testing](#id-unit-testing) <br/>
9. [GUI](#id-gui) <br/>
10. [Graphics](#id-graphics) <br/>
11. [Python Bindings](#id-pybind)<br/> 
12. [Resources](#id-resources) <br/>
	12.1. [Books](#id-books) <br/>
	12.2. [Links](#id-links) <br/>
13. [TODO List/ Next Steps](#id-todo) <br/>

*** 

<div id='id-basics'/>

## 1. Basics

<div id='id-basics-loops'/>

### 1.1. How to use for loops

```python

import sys
from copy import deepcopy
from mymodules import fibonacci #custom modules

### for loop

def forloops():
    name = input ("Name: ")
    i = 0 # acummulator pattern aka counter
    for c in name:
        print (c)
        i = i+1 
    print ("number of characters ", i)   
```

<div id='id-basics-deep'/>

### 1.2. Deep and shallow copy

```python

import sys
from copy import deepcopy
from mymodules import fibonacci #custom modules

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
	
if __name__ == "__main__":
	ShallowAndDeepCopy()
```

<div id='id-basics-modules'/>

### 1.3. Modules (Custom)

Create and import custom modules

```python

from mymodules import fibonacci #custom modules

if __name__ == "__main__":
	print ("Fibonacci: ", fibonacci.fib(10))

 # On folder "mymodules" the file fibonacy.py
 # Modular Programming 
 # https://www.python-course.eu/python3_modules_and_modular_programming.php

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
```


<div id='id-basics-lambdas'/>

### 1.4. Lambas

```python

# https://www.python-course.eu/python3_lambda.php

from functools import reduce

sum = lambda x, y: x+y
print (sum (2,4))


# reduce
# Determining the maximum of a list of numerical values by using reduce


g = lambda a,b: a if (a > b) else b
g = reduce( g,[47,11,42,102,13])
print (g)

# Calculating the sum of the numbers from 1 to 100
f = reduce (lambda x,y: x+y, range(1,101))
print (f)

```


<div id='id-basics-recursion'/>

### 1.5. Recursion

```python

import turtle

def drawSpiral(t, length, color, colorBase):
    if length == 0:
        return
    
    newcolor = (int(color[1:], 16)+2**10)%(2**24)
    base = int (colorBase[1:],16)

    if newcolor < base :
        newcolor  = (newcolor + base)%(2**24)

    newcolor = hex(newcolor)[2:]
    newcolor = "#"+("0"*(6-len(newcolor)))+newcolor
    t.color(newcolor)
    t.forward(length)
    t.left(90)

    drawSpiral(t, length-1, newcolor, colorBase)

def main():
    t = turtle.Turtle()
    screen = t.getscreen()
    t.speed(100)
    t.penup()
    t.goto(-100,-100)
    t.pendown()
    print ("main function")
    drawSpiral(t, 200,"#000000", "#ff00ff")
    screen.exitonclick()


if __name__ == "__main__":
    main()


```
<div id='id-copy'/>

### 1.6. Copy By Reference or Value


```python

def func(other):
    print ("func -> other before change: ", id(other))
    print (first is other)
    other = 2
    print ("func -> other after change: ",id(other))
    print (first is other)

first = 1
print (id(first))

func(first)

print (first)
print (id(first))
print ("=============")

# --------------------------------------------

def funcList(other):
    other[0] += 1
    print (lst is other)
    other += [1]
    print (lst is other)

lst = [1]
funcList(lst)
print (lst)

# imutable objects (int, str, long, tuples)
# mutables objctes (list, dictionaries)

```

<div id='id-static-class'/>

### 1.7. Instance, Class, and Static Methods]

```python

# class methods, static methods and instance methods
# https://realpython.com/instance-class-and-static-methods-demystified/
# https://www.geeksforgeeks.org/class-method-vs-static-method-python/ 

class Myclass:

    #. You can see the method takes one parameter, self, which points to an instance of MyClass when the method is called
    def method(self):
        return 'instance method called', self

    # has access to this cls argument, it cannot  modify object instance state
    # class methods can still modify class state that applies across all instances of the class
    # It can modify a class state that would apply across all the instances of the class. For example it can modify a class variable that will be applicable to all the instances.
    
    # ... python doesn’t support method overloading like C++ or Java so we use class methods to create factory methods. In the below example we use a class method to create a person object from birth year ... 
    @classmethod
    def classmethod(cls):
        return 'class methos called', cls

    # a static method can neither modify object state nor class state
    @staticmethod
    def staticmethod():
        return 'static method called'

obj = Myclass()
print (obj.method())
print (obj.staticmethod())

```
  
<div id='id-static-vars'/>
  
### 1.8. Class or Static Variables in Python

```python

# Code from: https://www.geeksforgeeks.org/g-fact-34-class-or-static-variables-in-python/

# Python program to show that the variables with a value 
# assigned in class declaration, are class variables 

# Class for Computer Science Student 
class CSStudent: 
	stream = 'cse'				 # Class Variable 
	def __init__(self,name,roll): 
		self.name = name		 # Instance Variable 
		self.roll = roll		 # Instance Variable 

# Objects of CSStudent class 
a = CSStudent('Geek', 1) 
b = CSStudent('Nerd', 2) 

print(a.stream) # prints "cse" 
print(b.stream) # prints "cse" 
print(a.name) # prints "Geek" 
print(b.name) # prints "Nerd" 
print(a.roll) # prints "1" 
print(b.roll) # prints "2" 

# Class variables can be accessed using class 
# name also 
print(CSStudent.stream) # prints "cse" 

```

<Div id='id-not-basics'/>

## 2. Not so basic

<div id='id-basics-reflection'/>

### 2.1. Reflection

```python

def reverse(seq):
    SeqType = type(seq)
    emptySeq = SeqType()

    if seq == emptySeq:
        return emptySeq

    #print("sequential vector = ", seq[1:])
    restrev = reverse(seq[1:])
    #print ("retrev = ", restrev)
    first = seq[0:1]
    #print ("first = ",first)
    restrev += first
    return restrev
        
def main():
    print(reverse([1,2, 3, 4]))
    #print(reverse("hello"))

if __name__ == "__main__":
    main()

```

<div id='id-basics-hooks'/>

### 2.2. Hooks

**TODO**




<div id='id-basics-yield'/>

### 2.3. yield and Generators

```Python

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

```

[Improve Your Python: 'yield' and Generators Explained](https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/)



"... The yield statement suspends function’s execution and sends a value back to caller, but retains enough state to enable function to resume where it is left off. When resumed, the function continues execution immediately after the last yield run. This allows its code to produce a series of values over time, rather them computing them at once and sending them back like a list. .."

```Python

def netxSquare():
    i = 1;
    while True:
        yield i*i
        i += 1

for num in netxSquare():
    if num > 10:
        break
    print (num)


```
 
" ... Yield are used in Python generators. A generator function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return. If the body of a def contains yield, the function automatically becomes a generator function. ..."

[When to use yield instead of return in Python?](https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/)

<div id='id-files'/>

## 2. Files

How to read and write files

```python

import sys

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
	
if __name__ == "__main__":
	ReadFromFile()
    WriteFromFile()
	
```

<div id='id-data'/>

## 4. Data-Structures

The built-ins data structures are: 
- lists
- tuples
- dictionaries
- strings 
- sets 

But we can create some custom made Data Structures

### Custom List

```python

#Customize a list in python

class PyList:
    def __init__(self, contents=[], size=10):
        self.items = [None]*size
        self.numItems = size
        self.size = size

        for e in contents:
            print ("Append = ", e)
            self.items.append(e)

    def print(self):
        for i in self.items:
            print(i)
    
    def printVersion2(self):
        idx = 0
        while idx < self.size-1:
            print ("value: ", self.items[idx], " at position :", idx)
            idx = idx + 1
        print()

    def __getitem__(self, index):
        if index >=0 and index < len(self.items):
            return self.items[index]
        raise IndexError ("PyList index out of range")
    
    def __setitem__(self, index,val):
        if index >=0 and index < len(self.items):
            self.items[index] = val
            return
        raise IndexError ("PyList index out of range")

    def __makeroom(self):
        newlen = (self.size // 4) + self.size + 1
        newlst = [None]  * newlen
        for i in range(self.numItems):
            newlst[i] = self.items[i]
        self.items = newlst
        self.size = newlen
    
    def append(self,item):
        if self.numItems == self.size:
            self.__makeroom()
        self.items[self.numItems] = item
        self.numItems +=1
    
    def __add_(self, other):
        result = PyList(size=self.numItems+other.numItems)
        for i in range(self.numItems):
            result.append(self.items[i])
        for i in range(other.numItems):
            result.append(self.items[i])
        return result 

    def __len__(self):
        return len(self.items)

if __name__ == "__main__":
    sample = PyList(["a", "b", "c"])
    sample.print()
    sample.printVersion2()
    #print ("Index value at 8 position: ", sample.__getitem__(11))
    sample.__setitem__(1, "w")
    sample.printVersion2()
    sample.append(["n","o"])
    sample.printVersion2()
    print ("Size of List: ",sample.__len__())
```

### Linked List

```python


# https://www.tutorialspoint.com/python/python_advanced_linked_list.htm


class LinkedList:
    class __Node:
            def __init__(self, item, next=None):
                self.item = item
                self.next = next
              
            def getItem(self):
                return self.item

            def getNext(self):
                return self.next

            def setItem(self, item):
                self.item = item
            
            def setNext (self, next):
                self.next = next
    
    def __init__(self, contents = []):
        self.first = LinkedList.__Node (None, None)
        self.last = self.first
        self.numItems = 0 

```

### Matrix

```python

# double list

class Board:
    matrix = []
    quadraticlimit = 0
    
    def __init__(self,board=None, limit = 3):
        self.quadraticlimit = 3
    
    def brutalWay(self):
        for i in range(self.quadraticlimit):
            self.matrix.append([])
            for j in range(self.quadraticlimit):
                self.matrix[i].append(i+j)

    def elegantWay(self):
        elegantMatrix = [[0 for y in range(self.quadraticlimit)] for x in range (self.quadraticlimit)]
        return elegantMatrix

    def print(self):
        for i in range(self.quadraticlimit):
            for j in range(self.quadraticlimit):
                print ("i=", i, "j= ", j ," => ", self.matrix[i][j]) 
            print ("")

if __name__ == "__main__":
    b = Board()
    b.brutalWay()
    b.print()
    print ("======================\n")
    b.elegantWay()
    b.print()

```

### Stack 

```python

class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        if self.isEmpty():
            raise RuntimeError ("Attempt to pop and empty stack")
        topIdx = len(self.items)-1
        item = self.items[topIdx]
        del self.items[topIdx]
        return item
    
    def top(self):
        if self.isEmpty():
            raise RuntimeError ("Attempt to get top of empty stack")
        topIdx = len (self.items)-1
        return self.items[topIdx]
    
    def push(self, item):
        self.items.append(item)
    
    def isEmpty(self):
        return len(self.items) == 0

def main():
    s = Stack()
    
    '''
    lst = list (range(10))
    lst = []  
    for k in lst:
        s.push(k)
    if s.top() == 9:
        print ("test 1 passed")
    else:
        print ("test 1 failed")
    ''' 
    s.push(55)

    print ("Get the top: ", s.top())


if __name__ == "__main__":
    main()
```

<div id='id-lc'>

### 4.1. List Comprehensions

```python

# avoid cycles

x = [i for i in range(10)]

for i in x:
    print (i)

# without list comprehensions

squares = []
for x in range(10):
    squares.append(x**2)

print (squares)

squares_lc = [x**2 for x in range(10)]
print (squares_lc)

```

[List Comprehensions in Python](https://www.pythonforbeginners.com/basics/list-comprehensions-in-python)

<div id='id-oo'/>

## 5. Object-Oriented

### 5.1. Create and print a simple class

```python
import turtle

class Dog:
        def __init__(self, name, year, speakText):
            self.name = name
            self.year = year
            self.speakText = speakText

        def get_speak(self):
            return self.speakText

        def get_name(self):

            return self.name

        def get_year(self):
            return self.year

def main():
    dog= Dog("Rasteirinho",2015,"wofwof")
    print (dog.get_name())
    print (dog.get_speak())
    t = turtle.Turtle()
    screen = t.getscreen()
    t.ht()
    screen.exitonclick()
    print ("Program Execution Completed")

if __name__ == "__main__":
    x=5
    y=2
    print("quotient: ",x/y)
    print("integer quotient: ",x//y)
    print("Remeinder: ",x%y)

    main()  
```



<div id='id-oo-inheritance' />

### 6. Inheritance and virtual class and methods

```python

# The imports include turtle graphics and tkinter modules. 
# The colorchooser and filedialog modules let the user
# pick a color and a filename.

import turtle
import tkinter
import tkinter.colorchooser
import tkinter.filedialog
import xml.dom.minidom

# The following classes define the different commands that 
# Are supported by the drawing application. 

class GoToCommand:
    def __init__(self,x,y,width=1,color="black"):
        self.x = x
        self.y = y
        self.width = width
        self.color = color
        
    # The draw method for each command draws the command
    # using the given turtle
    def draw(self,turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x,self.y)
        
    # The __str__ method is a special method that is called
    # when a command is converted to a string. The string
    # version of the command is how it appears in the graphics
    # file format. 
    def __str__(self):
        return '<Command x="' + str(self.x) + '" y="' + str(self.y) + \
               '" width="' + str(self.width) \
               + '" color="' + self.color + '">GoTo</Command>' 
        
class CircleCommand:
    def __init__(self,radius, width=1,color="black"):
        self.radius = radius
        self.width = width
        self.color = color
        
    def draw(self,turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.circle(self.radius)
        
    def __str__(self):
        return '<Command radius="' + str(self.radius) + '" width="' + \
               str(self.width) + '" color="' + self.color + '">Circle</Command>'
        
class BeginFillCommand:
    def __init__(self,color):
        self.color = color
        
    def draw(self,turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()
        
    def __str__(self):
        return '<Command color="' + self.color + '">BeginFill</Command>'
        
class EndFillCommand:
    def __init__(self):
        pass
    
    def draw(self,turtle):
        turtle.end_fill()
        
    def __str__(self):
        return "<Command>EndFill</Command>"
        
class PenUpCommand:
    def __init__(self):
        pass
    
    def draw(self,turtle):
        turtle.penup()
        
    def __str__(self):
        return "<Command>PenUp</Command>"
        
class PenDownCommand:
    def __init__(self):
        pass
    
    def draw(self,turtle):
        turtle.pendown()
        
    def __str__(self):
        return "<Command>PenDown</Command>"

# This is the container class for a graphics sequence. It is meant
# to hold the graphics commands sequence. 

class GraphicsSequence:
    def __init__(self):
        self.gcList = []
        
    # The append method is used to add commands to the sequence.
    def append(self,item):
        self.gcList = self.gcList + [item]
        
    # This method is used by the undo function. It slices the sequence
    # to remove the last item
    def removeLast(self):
        self.gcList = self.gcList[:-1]
       
    # This special method is called when iterating over the sequence.
    # Each time yield is called another element of the sequence is returned
    # to the iterator (i.e. the for loop that called this.)
    def __iter__(self):
        for c in self.gcList:
            yield c
    
    # This is called when the len function is called on the sequence.        
    def __len__(self):
        return len(self.gcList)
        
    # The write method writes an XML file to the given filename
    def write(self,filename):
        file = open(filename, "w")
        file.write('<?xml version="1.0" encoding="UTF-8" standalone="no" ?>\n')
        file.write('<GraphicsCommands>\n')
        for cmd in self:
            file.write('    '+str(cmd)+"\n")
            
        file.write('</GraphicsCommands>\n')
            
        file.close()  
        
    # The parse method adds the contents of an XML file to this sequence
    def parse(self,filename):
        xmldoc = xml.dom.minidom.parse(filename)
        
        graphicsCommandsElement = xmldoc.getElementsByTagName("GraphicsCommands")[0]
        
        graphicsCommands = graphicsCommandsElement.getElementsByTagName("Command")
        
        for commandElement in graphicsCommands:
            print(type(commandElement))
            command = commandElement.firstChild.data.strip()
            attr = commandElement.attributes
            if command == "GoTo":
                x = float(attr["x"].value)
                y = float(attr["y"].value)
                width = float(attr["width"].value)
                color = attr["color"].value.strip()
                cmd = GoToCommand(x,y,width,color)
    
            elif command == "Circle":
                radius = float(attr["radius"].value)
                width = int(attr["width"].value)
                color = attr["color"].value.strip()
                cmd = CircleCommand(radius,width,color)
    
            elif command == "BeginFill":
                color = attr["color"].value.strip()
                cmd = BeginFillCommand(color)
    
            elif command == "EndFill":
                cmd = EndFillCommand()
                
            elif command == "PenUp":
                cmd = PenUpCommand()
                
            elif command == "PenDown":
                cmd = PenDownCommand()
            else:
                raise RuntimeError("Unknown Command: " + command) 
    
            self.append(cmd)
            

# This class defines the drawing application. The following line says that
# the DrawingApplication class inherits from the Frame class. This means


class DrawingApplication(tkinter.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.buildWindow()    
        self.graphicsCommands = GraphicsSequence()
 
    # This method is called to create all the widgets, place them in the GUI,
    # and define the event handlers for the application.
    def buildWindow(self):
        
        # The master is the root window. The title is set as below. 
        self.master.title("Draw")
        
        # Here is how to create a menu bar. The tearoff=0 means that menus
        # can't be separated from the window which is a feature of tkinter.
        bar = tkinter.Menu(self.master)
        fileMenu = tkinter.Menu(bar,tearoff=0)
        
        # This code is called by the "New" menu item below when it is selected.
        # The same applies for loadFile, addToFile, and saveFile below. The 
        # "Exit" menu item below calls quit on the "master" or root window. 
        def newWindow():
            # This sets up the turtle to be ready for a new picture to be 
            # drawn. It also sets the sequence back to empty. It is necessary
            # for the graphicsCommands sequence to be in the object (i.e. 
            # self.graphicsCommands) because otherwise the statement:
            # graphicsCommands = GraphicsSequence()
            # would make this variable a local variable in the newWindow 
            # method. If it were local, it would not be set anymore once the
            # newWindow method returned.
            theTurtle.clear()
            theTurtle.penup()
            theTurtle.goto(0,0)
            theTurtle.pendown()  
            screen.update()
            screen.listen()
            self.graphicsCommands = GraphicsSequence()
            
        fileMenu.add_command(label="New",command=newWindow)
            
        def loadFile():

            filename = tkinter.filedialog.askopenfilename(title="Select a Graphics File")
            
            newWindow()
            
            # This re-initializes the sequence for the new picture. 
            self.graphicsCommands = GraphicsSequence()
            
            # calling parse will read the graphics commands from the file.
            self.graphicsCommands.parse(filename)
               
            for cmd in self.graphicsCommands:
                cmd.draw(theTurtle)
                
            # This line is necessary to update the window after the picture is drawn.
            screen.update()
            
            
        fileMenu.add_command(label="Load...",command=loadFile)
        
        def addToFile():
            filename = tkinter.filedialog.askopenfilename(title="Select a Graphics File")
            
            theTurtle.penup()
            theTurtle.goto(0,0)
            theTurtle.pendown()
            theTurtle.pencolor("#000000")
            theTurtle.fillcolor("#000000")
            cmd = PenUpCommand()
            self.graphicsCommands.append(cmd)
            cmd = GoToCommand(0,0,1,"#000000")
            self.graphicsCommands.append(cmd)
            cmd = PenDownCommand()
            self.graphicsCommands.append(cmd)
            screen.update()
            self.graphicsCommands.parse(filename)
               
            for cmd in self.graphicsCommands:
                cmd.draw(theTurtle)
                
            screen.update()            
        
        fileMenu.add_command(label="Load Into...",command=addToFile)
        
        def saveFile():
            filename = tkinter.filedialog.asksaveasfilename(title="Save Picture As...")
            self.graphicsCommands.write(filename)
            
        fileMenu.add_command(label="Save As...",command=saveFile)
        

        fileMenu.add_command(label="Exit",command=self.master.quit)
        
        bar.add_cascade(label="File",menu=fileMenu)
        
        # This tells the root window to display the newly created menu bar.
        self.master.config(menu=bar)    
        
        # Here several widgets are created. The canvas is the drawing area on 
        # the left side of the window. 
        canvas = tkinter.Canvas(self,width=600,height=600)
        canvas.pack(side=tkinter.LEFT)
        
        # By creating a RawTurtle, we can have the turtle draw on this canvas. 
        # Otherwise, a RawTurtle and a Turtle are exactly the same.
        theTurtle = turtle.RawTurtle(canvas)
        
        # This makes the shape of the turtle a circle. 
        theTurtle.shape("circle")
        screen = theTurtle.getscreen()
        
        # This causes the application to not update the screen unless 
        # screen.update() is called. This is necessary for the ondrag event
        # handler below. Without it, the program bombs after dragging the 
        # turtle around for a while.
        screen.tracer(0)
    
        # This is the area on the right side of the window where all the 
        # buttons, labels, and entry boxes are located. The pad creates some empty 
        # space around the side. The side puts the sideBar on the right side of the 
        # this frame. The fill tells it to fill in all space available on the right
        # side. 
        sideBar = tkinter.Frame(self,padx=5,pady=5)
        sideBar.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
        
        # This is a label widget. Packing it puts it at the top of the sidebar.
        pointLabel = tkinter.Label(sideBar,text="Width")
        pointLabel.pack()
        
        # This entry widget allows the user to pick a width for their lines. 
        # With the widthSize variable below you can write widthSize.get() to get
        # the contents of the entry widget and widthSize.set(val) to set the value
        # of the entry widget to val. Initially the widthSize is set to 1. str(1) is 
        # needed because the entry widget must be given a string. 
        widthSize = tkinter.StringVar()
        widthEntry = tkinter.Entry(sideBar,textvariable=widthSize)
        widthEntry.pack()
        widthSize.set(str(1))
        
        radiusLabel = tkinter.Label(sideBar,text="Radius")
        radiusLabel.pack()
        radiusSize = tkinter.StringVar()
        radiusEntry = tkinter.Entry(sideBar,textvariable=radiusSize)
        radiusSize.set(str(10))
        radiusEntry.pack()
        
        # A button widget calls an event handler when it is pressed. The circleHandler
        # function below is the event handler when the Draw Circle button is pressed. 
        def circleHandler():
            # When drawing, a command is created and then the command is drawn by calling
            # the draw method. Adding the command to the graphicsCommands sequence means the
            # application will remember the picture. 
            cmd = CircleCommand(int(radiusSize.get()), int(widthSize.get()), penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            
            # These two lines are needed to update the screen and to put the focus back
            # in the drawing canvas. This is necessary because when pressing "u" to undo,
            # the screen must have focus to receive the key press. 
            screen.update()
            screen.listen()
        
        # This creates the button widget in the sideBar. The fill=tkinter.BOTH causes the button
        # to expand to fill the entire width of the sideBar.
        circleButton = tkinter.Button(sideBar, text = "Draw Circle", command=circleHandler)
        circleButton.pack(fill=tkinter.BOTH)             

        # The color mode 255 below allows colors to be specified in RGB form (i.e. Red/
        # Green/Blue). The mode allows the Red value to be set by a two digit hexadecimal
        # number ranging from 00-FF. The same applies for Blue and Green values. The 
        # color choosers below return a string representing the selected color and a slice
        # is taken to extract the #RRGGBB hexadecimal string that the color choosers return.
        screen.colormode(255)
        penLabel = tkinter.Label(sideBar,text="Pen Color")
        penLabel.pack()
        penColor = tkinter.StringVar()
        penEntry = tkinter.Entry(sideBar,textvariable=penColor)
        penEntry.pack()
        # This is the color black.
        penColor.set("#000000")  
        
        def getPenColor():
            color = tkinter.colorchooser.askcolor()
            if color != None:
                penColor.set(str(color)[-9:-2])
            
        penColorButton = tkinter.Button(sideBar, text = "Pick Pen Color", command=getPenColor)
        penColorButton.pack(fill=tkinter.BOTH)           
            
        fillLabel = tkinter.Label(sideBar,text="Fill Color")
        fillLabel.pack()
        fillColor = tkinter.StringVar()
        fillEntry = tkinter.Entry(sideBar,textvariable=fillColor)
        fillEntry.pack()
        fillColor.set("#000000")     
        
        def getFillColor():
            color = tkinter.colorchooser.askcolor()
            if color != None:    
                fillColor.set(str(color)[-9:-2])       
   
        fillColorButton = \
            tkinter.Button(sideBar, text = "Pick Fill Color", command=getFillColor)
        fillColorButton.pack(fill=tkinter.BOTH) 


        def beginFillHandler():
            cmd = BeginFillCommand(fillColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            
        beginFillButton = tkinter.Button(sideBar, text = "Begin Fill", command=beginFillHandler)
        beginFillButton.pack(fill=tkinter.BOTH) 
        
        def endFillHandler():
            cmd = EndFillCommand()
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)
            
        endFillButton = tkinter.Button(sideBar, text = "End Fill", command=endFillHandler)
        endFillButton.pack(fill=tkinter.BOTH) 
 
        penLabel = tkinter.Label(sideBar,text="Pen Is Down")
        penLabel.pack()
        
        def penUpHandler():
            cmd = PenUpCommand()
            cmd.draw(theTurtle)
            penLabel.configure(text="Pen Is Up")
            self.graphicsCommands.append(cmd)

        penUpButton = tkinter.Button(sideBar, text = "Pen Up", command=penUpHandler)
        penUpButton.pack(fill=tkinter.BOTH) 
       
        def penDownHandler():
            cmd = PenDownCommand()
            cmd.draw(theTurtle)
            penLabel.configure(text="Pen Is Down")
            self.graphicsCommands.append(cmd)

        penDownButton = tkinter.Button(sideBar, text = "Pen Down", command=penDownHandler)
        penDownButton.pack(fill=tkinter.BOTH)          

        # Here is another event handler. This one handles mouse clicks on the screen.
        def clickHandler(x,y): 
            # When a mouse click occurs, get the widthSize entry value and set the width of the 
            # pen to the widthSize value. The int(widthSize.get()) is needed because
            # the width is an integer, but the entry widget stores it as a string.
            cmd = GoToCommand(x,y,int(widthSize.get()),penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)          
            screen.update()
            screen.listen()
           
        # Here is how we tie the clickHandler to mouse clicks.
        screen.onclick(clickHandler)  
        
        def dragHandler(x,y):
            cmd = GoToCommand(x,y,int(widthSize.get()),penColor.get())
            cmd.draw(theTurtle)
            self.graphicsCommands.append(cmd)  
            screen.update()
            screen.listen()
            
        theTurtle.ondrag(dragHandler)
        
        # the undoHandler undoes the last command by removing it from the 
        # sequence and then redrawing the entire picture. 
        def undoHandler():
            if len(self.graphicsCommands) > 0:
                self.graphicsCommands.removeLast()
                theTurtle.clear()
                theTurtle.penup()
                theTurtle.goto(0,0)
                theTurtle.pendown()
                for cmd in self.graphicsCommands:
                    cmd.draw(theTurtle)
                screen.update()
                screen.listen()
                
        screen.onkeypress(undoHandler, "u")
        screen.listen()


# The main function in our GUI program is very simple. It creates the 
# root window. Then it creates the DrawingApplication frame which creates 
# all the widgets and has the logic for the event handlers. Calling mainloop
# on the frames makes it start listening for events. The mainloop function will 
# return when the application is exited. 


def main():
    root = tkinter.Tk()  
    drawingApp = DrawingApplication(root)  

    drawingApp.mainloop()
    print("Program Execution Completed.")
        
if __name__ == "__main__":
    main()

``` 


### Another Example of class Inheritance

```python

# https://www.tutorialspoint.com/python/python_classes_objects.htm
# https://realpython.com/python3-object-oriented-programming/
# https://www.python-course.eu/python3_abstract_classes.php
# https://www.python-course.eu/python3_object_oriented_programming.php

# Normal class


class Employee:
    #class attributes
   empCount = 0
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)



# Class Inheritance
# Naming   Type       Meaning
# ----------------------------------
# name	 Public     These attributes can be freely used inside or outside of a class definition.
# _name	 Protected  Protected attributes should not be used outside of the class definition, unless # inside of a subclass definition. 
# __name	 Private    This kind of attribute is inaccessible and invisible. It's neither possible to read nor write to those attributes, except inside of the class definition itself.


class Parent:        # define parent class
    parentAttr = 100
    visibleParam = 15
    __hiddenParam = 12 #double __ hides parameter
    def __init__(self):
       print ("Calling parent constructor")
    
    def __del__(self):
       print ("Parent has been destroyed")

    def parentMethod(self):
       print ('Calling parent method')

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print ("Parent attribute :", Parent.parentAttr)
    
    def myMethod(self):
        print ("Parent class: myMethod")

class Child(Parent): # define child class
    def __init__(self):
       print ("Calling child constructor")
    
    def __del__(self):
       super(Child, self).__del__() # important to invoke parents destructor
       print ("Child has been destroyed")

    def childMethod(self):
       print ('Calling child method')
    
    def myMethod(self):
       print ("Child class: myMethod")

# Abstrack class

class AbstractClassExample():
    def doSomething(self):
        print("AbstractClassExample:Some implementation !")

class AnotherSubclass(AbstractClassExample):
        def doSomething(self):
            super().doSomething()
            print("AnotherSubclass:Some implementation !")

if __name__ == "__main__":

    an = AnotherSubclass()
    an.doSomething()

    e1 = Employee("Zara", 23)
    e1.displayCount()
    e1.displayEmployee()
    e2 = Employee("Ann", 31)
    print("Number of employees: ", Employee.empCount)
    print("Employee.__doc__:", Employee.__doc__)
    print("Employee.__name__:", Employee.__name__)
    print("Employee.__module__:", Employee.__module__)
    print("Employee.__bases__:", Employee.__bases__)
    print("Employee.__dict__:", Employee.__dict__)

    print ("Same instances: ", e1 == e2,"  ",e1,"  ",e2)
    print ("Internal class dictionary: ", e1.__dict__ )

    c = Child()          # instance of child
    c.childMethod()      # child calls its method
    c.parentMethod()     # calls parent's method
    c.setAttr(200)       # again call parent's method
    c.getAttr()          # again call parent's method
    
    c = Child()
    c.myMethod() # child calls overriden method

    #c.__hiddenParam()
    print("Check parent visible params: ",c.visibleParam)

```


<div id='id-math'/>

## 6. Math

<div id='id-numpy'/>

### 6.1 numpy

"... NumPy is a Python package. It stands for 'Numerical Python'. It is a library consisting of multidimensional array objects and a collection of routines for processing of array ..."

```python
import numpy as np

a = np.array([1, 2,3])
print (a)

```

Source and Quotes from [Learn NumPy - absolute beginners](https://www.tutorialspoint.com/numpy/)

<div id='id-network'/>

## 7. Network

<div id='id-network-echo-server' />

### 7.1. Simple server-client echo application for one connection.

Source code from [Socket Programming in Python (Guide)](https://realpython.com/python-sockets/)

**Server**

```python


# echo server - client
# source code from here -> https://realpython.com/python-sockets/

import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print ('connceted by: ', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
```


**Client**

```python


# echo server - client
# source code from here -> https://realpython.com/python-sockets/


import socket

HOST = '127.0.0.1'
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'Hello from client script')
    data = s.recv(1024)

print ('Received reply(echo) from server: ', repr(data))

```

### Other links

https://medium.com/swlh/lets-write-a-chat-app-in-python-f6783a9ac170

https://steelkiwi.com/blog/working-tcp-sockets/


<div id='id-arch'/>

## 8. Software-Architecture

* Notes from book:  Software Architecture with Python - Anand Balachandran Pillai

This is a broad topic but is always nice to quick explore the behaviour and possibilities in these topics:

- refactoring
- testability
- performance 
- scale applications
- security
- design patterns

*... Modifiability is the degree of ease at which changes can be made to a system, and the flexibility with which the system adapts to such changes..."*

*...The late binding refers to the practice of postponing the binding of values to parameters as late as possible in the order of execution of a code. Late binding allows the programmer to defer the factors which influence code execution, and hence the results of execution and performance of the code, to a later time by making use of multiple techniques..."*

<div id='id-unit-testing'/>

### 8.1 Unit-Testing

" ... 

To achieve this, unittest supports some important concepts:

**test fixture**
    A test fixture represents the preparation needed to perform one or more tests, and any associate cleanup actions. This may involve, for example, creating temporary or proxy databases, directories, or starting a server process.

**test case**
    A test case is the smallest unit of testing. It checks for a specific response to a particular set of inputs. unittest provides a base class, TestCase, which may be used to create new test cases.

**test suite**
    A test suite is a collection of test cases, test suites, or both. It is used to aggregate tests that should be executed together.

**test runner**
    A test runner is a component which orchestrates the execution of tests and provides the outcome to the user. The runner may use a graphical interface, a textual interface, or return a special value to indicate the results of executing the tests

..."

-> quote from: Software Architecture with Python - Anand Balachandran Pillai

```python

import unittest

class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_split(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper()) 

if __name__== '__main__':
    unittest.main()

```

[ unittest — Unit testing framework ](https://docs.python.org/2/library/unittest.html)

<div id='id-gui'/>

## 9. GUI

[Tkinter](https://wiki.python.org/moin/TkInter)

[PyQt](https://wiki.python.org/moin/PyQt)

<div id='id-graphics'/>

## 10. Graphics

[Python + OpenGL](https://github.com/NelsonBilber/py.opengl)

<div id='id-resources'/>


<div id='id-pybind'>

## 11. Python Bindings

One cool feature in Python is the possibility of creating binding from libraries developed in other languages, e.g. C and C++.
We cloud use well establish libraries with years of development and easily use them without deal with low level code details.

[pybind11](https://github.com/pybind/pybind11)

Some Examples:

[pymesh](https://pymesh.readthedocs.io/en/latest/)

[libigl](https://github.com/libigl/libigl)


## 12. Resources

<div id='id-books'/>

### 12.1. Books

**Some of code source examples are the study result/extracted from next books**:

- Python Programming Fundamentals - Ken D. Lee
- Data Structures and Algorithms with Python - Ken D. Lee
- Software Architecture with Python - Anand Balachandran Pillai

<div id='id-links'/>

### 12.2. Links

[Learn Python the Hard Way](https://learnpythonthehardway.org/python3/) My solutions [here](https://github.com/NelsonBilber/py.thehardway)

[Best Python Resources](https://www.fullstackpython.com/best-python-resources.html)

<div id='id-todo'/>

## 13. TODO List/ Next Steps

Some tips from my co-workers next steps cloud be:

- [ ] tensors [read](https://www.datacamp.com/community/tutorials/investigating-tensors-pytorch)
- [ ] improve for loop e.g. use enumerates
- [ ] seaborn
- [ ] matplotlib
- [ ] pandas
- [ ] concurrency and multi-threading, async, wait, 

