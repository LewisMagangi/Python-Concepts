from dataclasses import dataclass

@dataclass
class Employee:
    name: str
    department: str
    salary: int

john = Employee('john', 'Informatics', 1000)
print(f'{john.name} whose salary is {john.salary} works in the {john.department} department')
