#https://www.tutorialspoint.com/python/python_classes_objects.htm
#https://realpython.com/python3-object-oriented-programming/
#https://www.python-course.eu/python3_abstract_classes.php
#https://www.python-course.eu/python3_object_oriented_programming.php

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

#------------------------------------------------------------------
# Class Inheritance


#Naming   Type       Meaning
#----------------------------
#name	 Public     These attributes can be freely used inside or outside of a class definition.
#_name	 Protected  Protected attributes should not be used outside of the class definition, unless inside of a subclass definition. 
#__name	 Private    This kind of attribute is inaccessible and invisible. It's neither possible to read nor write to those attributes, except inside of the class definition itself.

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
#------------------------------------------------------------------

class AbstractClassExample():
    def doSomething(self):
        print("AbstractClassExample:Some implementation !")

class AnotherSubclass(AbstractClassExample):
        def doSomething(self):
            super().doSomething()
            print("AnotherSubclass:Some implementation !")



#------------------------------------------------------------------
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