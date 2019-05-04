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

   