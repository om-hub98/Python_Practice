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

print("=======Employee Object Created=========================")
rocky = Employee("Rocky", 27, 50000)
nick = Employee("Nick", 25, 60000)


rocky.greet()
rocky.salary = 70000  # Updating salary for Rocky
Employee._location = "Kolkata"  # Updating protected variable - location for Rocky 
                                # N.B: This change will affect all instances of the Employee class, including Nick.
Employee.__sector = "Finance"  # Attempting to update private variable - sector for Rocky 
                                # N.B: This change will not affect the original private variable in the Employee class.
rocky.display()
print("================================")
nick.greet()
nick.display()
print("================================")