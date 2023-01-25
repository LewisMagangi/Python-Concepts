class Employee:

    num_of_employees = 0
    raise_amount = 1.02

    def __init__(self, firstname, lastname, payamount):
        self.firstname = firstname
        self.lastname = lastname
        self.email = firstname + "." + lastname + "gmail.com"
        self.payamount = payamount

    def print_fullname(self):
        print("{} {}".format(self.firstname, self.lastname))

    def print_email(self):
        print("{}".format(self.email))

    def print_applied_raise(self):
        self.payamount = int(self.payamount * self.raise_amount)

    """
    A class method that takes the class as the first argument
    """
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount


    """
    Using a class method as an alternative constructor
    """
    @classmethod
    def from_string(cls, emp_str):
        firstname, lastname, payamount = emp_str.split(".")
        return cls(firstname, lastname, payamount)

    """
    illustration of a static method(that doesn't parse the instance or the class as the 1st argument)
    """
    @staticmethod
    def is_weekend(day):
        if day.weekday() != 5 and day.weekday() != 6:
            return False
        return True

emp_str_1 = Employee("lewis", "mwaura", 50000)
emp_str_2 = Employee("liaam", "mwira", 90000)
emp_str_3 = Employee("kikky", "orwa", 40000)

Employee.set_raise_amount(1.30)

print(Employee.raise_amount)
print(emp_str_2.raise_amount)
print(emp_str_3.firstname)
            
import datetime
date = datetime.date(2023, 1, 25)

print("Today is on weekend") if Employee.is_weekend(date) else print("Today is a weekday")
