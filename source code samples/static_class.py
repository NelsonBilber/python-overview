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
