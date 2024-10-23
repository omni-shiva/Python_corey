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
        
class Developer(Employee): # Way to Create Subclass , this will get all the methods of Employee Class.
    raise_amt = 1.10 # This change will only get affected in Developer Subclass.
    def __init__(self,first,last,pay,prog_lang):
        super().__init__(first,last,pay)
        # Employee.__init__(self,self,first,last,pay) this is another way to use it. when mutiple inheritence there.
        self.prog_lang = prog_lang
        


"""Here even though we didnt put any init method for developers
its giving the data, bcz once we are initialising the Developer(...)
its first search for its own init method , then it will go to the above inheritence,
unless it find all the instances.

Now this chain is called Method Resolution Order, help function make it easier to visualise.
"""

dev_1 = Developer('corey','schafer',50000,'python')
dev_2 = Developer('test','user',6000,'java')

# print(help(Developer))

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# print(dev_1.fullname())
# print(dev_1.prog_lang)


print('Begin Manager subclass')

class Manager(Employee):
    def __init__(self,first,last,pay,employees = None): # We should never pass a mutable data types like list/dict as defualy arguments.
        super().__init__(first,last,pay)
        # Employee.__init__(self,self,first,last,pay) this is another way to use it. when mutiple inheritence there.
        if employees is None:
            self.employess = []
        else:
            self.employess = employees
    
    def add_emp(self,emp):
        if emp not in self.employess:
            self.employess.append(emp)
            
    def remove_emp(self,emp):
        if emp in self.employess:
            self.employess.remove(emp)
    
    def print_emps(self):
        for emp in self.employess:
            print('-->',emp.fullname())

mgr_1  = Manager('Sue','Smith',90000,[dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)
mgr_1.print_emps()

############################################
"isinstance() and issubclass() , two built-in functions in python"

print(isinstance(mgr_1,Employee))    # It will tell us if an object is an instance of a class.
print(issubclass(Developer,Employee))                 # If a class is a subclass of another.