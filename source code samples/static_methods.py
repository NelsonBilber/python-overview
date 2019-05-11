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
