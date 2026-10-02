from oops.association.employee import Employee
from typing import List

class Company:
    name: str
    employees: List[Employee]

    def __init__(self, name: str, employees: List[Employee]):
        self.name = name
        self.employees = employees