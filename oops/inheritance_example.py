class Parent:
    def __init__(self, name):
        self.name = name

    def greet_parent(self):
        return f"Hello from {self.name}!"


class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet_parent(self):
        parent_greeting = super().greet_parent()
        return f"{parent_greeting} and I am {self.age} years old!"

    def greet(self):
        return f"Hello from {self.name}, I am {self.age} years old!"

parent = Parent("Parent Class")
child = Child("Child Class", 10)

print(parent.greet_parent())
print(child.greet_parent())
#print(child.greet())