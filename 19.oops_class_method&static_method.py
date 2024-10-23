"""Regular Method , Class Method and Static Method"""
"""So Regualr method in a class automatically take the instance as the first argument i.e self we are calling it by convention """
class Employee:
    num_of_emps = 0
    raise_amt = 1.04
    def __init__(self,first,last,pay): 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps+= 1
        """this will count number of times __init__ got initiated , that is = number of times new emp getting added in self"""
        
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
    """#Class Method"""
    @classmethod # like self for regular method , CLS used to call classmethod
    def set_raise_amt(cls,amount): 
        cls.raise_amt = amount
        
    @classmethod # using class method as alternative constructor . Example - 2 
    def from_string(cls,emp_str):
        first,last,pay = emp_str.split('-')
        return cls(first,last,pay)
    
    @staticmethod #its simply behave like regular function
    def is_workday(day):
        if day.weekday()== 5 or day.weekday() == 6:
            return False
        return True
        
    
        

"""Class Method will take class as the first argument, to turn regular method to the classmethod just use @classmethod decorator"""

"""A method is a STATIC method if we don't access the instance or the class anywhere within the function, if there is no self variable 
so probably it will be a static method
"""

emp_1 = Employee('corey','schafer',50000)
emp_2 = Employee('test','user',6000)

# Example  - 1 for class method
# Employee.set_raise_amt(1.05)  # Running the class method from the instance like emp_1.set_raise_amt(1.05), will still work for all the object

"""here we dont need to mention for which instance like Employee.raise_amt(emp_1) , bcz class is automatically get passed here by class method.
"""
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)
# print(Employee.raise_amt)

"Example- 2  for alternative decorator use of class method"

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smit-30000'

# new_emp = Employee.from_string(emp_str_1)

# print(new_emp.email)

"Example - 3 for static method"

import datetime
my_date = datetime.date(2024,10,12)

print(Employee.is_workday(my_date))













