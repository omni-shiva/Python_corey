class Employee:
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self,first,last,pay): 
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
        Employee.num_of_emps+= 1  # this will count number of times __init__ got initiated , that is = number of times new emp getting added in self
        
    def fullname(self): 
        return '{} {}'.format(self.first,self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)   

emp_1 = Employee('corey','schafer',50000)
emp_2 = Employee('test','user',6000)

"""instance variable are unique for each instance but class variable should be the same for each instance.
class variables are variables that are shared among all instances of the class"""


# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)

# # print(emp_1.__dict__)

# emp_1.raise_amount = 1.05 # not it will only change for emp_1

# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
# print(Employee.raise_amount)


# RAISE IN emp , WHICH WILL BE REFELCTED IN INIT ALWAYS

print(Employee.num_of_emps)
