class Employee:
    def __init__(self,first,last): 
        self.first = first
        self.last = last
    @property # now we dont need to call email as function , we can use it as instance.
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first,self.last)   
    
    @fullname.setter # THIS WILL BE NEEDING TO CALL THE INSTANCE
    def fullname(self,name):
        first,last = name.split(' ')
        self.first = first
        self.last = last
        
    @fullname.deleter # to delete , this will run when we use del for full name
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
    
emp_1 = Employee('John','Smith')

emp_1.first = 'jim' # NOW WE can see that , email not changing to jim , bcz its fixed and only run when first time object emp_1 was made.

# Now in below example lets say we are setting the full name and then we want to change the first and last name accordingly. 

emp_1.fullname = 'Corey Schafer' # Error - property 'fullname' of 'Employee' object has no setter


print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname  #  @fullname.deleter  , here deleter will be used

