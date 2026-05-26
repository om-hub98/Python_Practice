class Person:

    ## Constructor to initialize the object
    def __init__(self, name, age):
        self.name = name      # instance variable
        self.age = age

    # Method declaration in python
    def greet(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old")

# Creating object
p1 = Person("Omraj", 27)

# Calling method
p1.greet()

p1 = Person("Niraj", 25);
p1.greet()