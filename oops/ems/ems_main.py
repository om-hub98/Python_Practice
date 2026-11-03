from oops.ems.employee import Employee


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