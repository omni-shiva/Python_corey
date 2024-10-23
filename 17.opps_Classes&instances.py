#Python object-Oriented 
#Method means  -A function associated with class.


class Employee:
    def __init__(self,first,last,pay): # init method(initialize) or constructor take the instances self, first , last  and pay or we can say all 3 are attribue
        self.first = first # its same as emp.first = first ( i.e Corey)
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        
    def fullname(self): # without  self it will give error , bcz we have to expect that instance arrgument in our method.
        return '{} {}'.format(self.first,self.last)
        
        

emp_1 = Employee('corey','schafer',50000) 
emp_2 = Employee('test','user',6000)

# print(emp_1)
# print(emp_2)


print(emp_1.email)
print(emp_2.email)
print(emp_2.fullname())  #here we need to put () bcz instead of attribute above , its an method or we can say we are calling a function.
# here emp_2.fullname will go internally like this.
print(Employee.fullname(emp_2)) # Here is regular method we need to pass instance for the method of a class.


#Example:-

class Emp:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.'+ last + '@hp.com'
    
    def fname(self):
        return '{} {}'.format(self.first,self.last)

emp_1 = Emp('shiva','kumar',50000)
print(emp_1.email)

print(emp_1.fname())