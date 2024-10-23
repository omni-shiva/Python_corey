# .sort() method will

li = [9,1,8,2,7,3,6,4,5]
s_li = sorted(li,reverse=True) # So here still its not changing the orignal, its setting  up new list.
print('Sorted Variable:\t', s_li) # This is  sorted function
print('Orignal Variable:\t', li)

#Sorting the orginal list of numbers without creating a new variable.

li.sort(reverse=True) #THIS IS sort method.
print('Orignal Variable:\t', li)

##=======================================#####
# We have a tuples below
tup = (9,1,8,2,7,3,6,4,5) # SO tuple doesn't have a sort method.
# tup.sort() # SO this method  will give error.
s_tup = sorted(tup)
'SO this will be s_tup is a list , and the value that are tuple that are sorted'
print('Tuple\t',s_tup)


##########**With dictionary**############

di = {'name':'Corey','job':'programming','age':None, 'os':'Mac'}
s_di = sorted(di)
print('Dict\t',s_di) # So this willl sort only the key with ascending order and return the list.

#######################
"Sorting on Absolute Value"

li = [-6,-5,1,2,3]
s_li = sorted(li,key = abs) #Now it wil give absolute as it runs each element beofre sorting to the abs.
print(s_li) # It wiill give the same order starting from negative.

            #NOTE# - 
###**SORTING IN CLASS**#######
"""Based on custom function,Lambda and attrgetter
"""
class Employee():
    def __init__(self,name ,age,salary):
        self.name =name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

e1 = Employee('corey','schafer',50000) 
e2 = Employee('priya','M',60000)
e3 = Employee('shiva','kumar',100000)   


# PUTTING the all the e1/e2/e3 in List.
employee = [e1,e2,e3]
s_employee = sorted(employee) # So running it without a key , its not really gonna know , how to sort them. so it will give error.
print(s_employee)

##This will give error . so we need to use key to sort this 
#Key -  OUR key takes a function that takes each element of our list  and returns what we want to sort on.

'Sorting  by creating key'
class Employee():
    def __init__(self,name ,age,salary):
        self.name =name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

e1 = Employee('corey','schafer',50000) 
e2 = Employee('priya','M',60000)
e3 = Employee('shiva','kumar',100000)


def e_sort(emp):
    return emp.name #BASED ON NAME

# now we can pass the key 

employee = [e1,e2,e3]
s_employee = sorted(employee,key = e_sort,reverse=True) 
print(s_employee)


'Sorting  by lambda'
class Employee():
    def __init__(self,name ,age,salary):
        self.name =name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

e1 = Employee('corey','schafer',50000) 
e2 = Employee('priya','M',60000)
e3 = Employee('shiva','kumar',100000)

# We dont need function here

# now we can pass the key 

employee = [e1,e2,e3]
s_employee = sorted(employee,key = lambda e: e.name  )  # Lambda , just create the anonymus function.
print(s_employee)


'Sorting  by attrgetter'
from operator import attrgetter

class Employee():
    def __init__(self,name ,age,salary):
        self.name =name
        self.age = age
        self.salary = salary
    
    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)

e1 = Employee('corey','schafer',50000) 
e2 = Employee('priya','M',60000)
e3 = Employee('shiva','kumar',100000)

# We dont need function here

# now we can pass the key 

employee = [e1,e2,e3]
s_employee = sorted(employee,key = attrgetter('age'))  # Lambda , just create the anonymus function.
print(s_employee)