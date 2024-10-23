"""Dunder init means init  surrounded by __ i.e Double Underscore"""

class Employee:
    raise_amt = 1.04
    def __init__(self,first,last,pay): 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        
    def __repr__(self):
        return "Employee('{}','{}', {} )".format(self.first,self.last,self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(),self.email)
    

     
"""Two more common special methods that we should probably always implement are __repr__(self) and __str__(self) , 
So order wise __str__ will try to take value first then __repr__ .
"""

emp_1 = Employee('corey','schafer',50000)
emp_1 = Employee('test','user',6000)

print(repr(emp_1))
print(str(emp_1))

"""Or we can write it like this"""

print(emp_1.__repr__())
print(emp_1.__str__())
