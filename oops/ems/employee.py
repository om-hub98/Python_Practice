class Employee:
    company_name = "TechCorp"  # Class variable shared by all instances
    _location = "New York"  # Protected class variable
    __sector = "Technology"  # Private class variable
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
        Employee.__sector = "BPO"  # Attempting to change the private class variable within the constructor

    def greet(self):
        Employee.__sector = "BPO-IT"  # Attempting to change the private class variable within the method
        print(f"Hi, I'm {self.name} and ",
              f"I am {self.age} years old and ",
              f"my salary is {self.salary} and ",
              f"I work at {Employee.company_name} ",
              f"located in {Employee._location}",
              f"currently in the {Employee.__sector} sector."
            )

    def display(self):
        print(f"Name: {self.name} ", 
              f"Age: {self.age} ", 
              f"Salary: {self.salary} ", 
              f"Company: {Employee.company_name} ", 
              f"Location: {Employee._location} ",
                f"Sector: {Employee.__sector}"
            )