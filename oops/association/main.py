from oops.association.employee import Employee
from oops.association.company import Company

employee1 = Employee("Omraj", 50)
employee2 = Employee("Abc", 47)

company = Company("ZZZ", [employee1, employee2])

print(company.employees[1].name)