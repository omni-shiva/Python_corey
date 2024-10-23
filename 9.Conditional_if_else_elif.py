if True:
    print('Conditional was True') # it will only be true , iff if is true
    
#===============================

#Comparisons:
#Equal:             ==
#Not Equal:         !=
#Greater Than:      >
#Less Than:         <
#Greater or Equal:  >=
#Less or Equal:     <=
#object Identity:   is

language = 'Java'
if language == 'Python':
    print('Language is Python')
elif language == 'Java':
    print('Language is Java')
else:
    print('No Match')
    
    
#Boolean Operatation

#and
#or
#not - it used to switch a boolean, True to flase and Flase to True.

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
    
"""In our code, both logged_in and logged_in == True are equivalent, 
but writing logged_in is cleaner and more Pythonic. Similarly, 
if we wanted to check if a variable is False, 
we would just use if not logged_in: rather than if logged_in == False:"""

#############################

# Obejct Identity - IS KEYWORD

a = [1,2,3]
b = [1,2,3]
print(a==b)
print(id(a))
print(id(b))
print(a is b) # its false bcz these are 2 different object in memory and having diff id ,
# So [is] comparision actually  checking whether the id is same or different.

a = [1,2,3]
b = a
print(a==b)
print(id(a))
print(id(b))
print(a is b)  # NOW  a and b have same object and its same as print(id(a) == id(b))
print(id(a) == id(b))


# False Values:
#Flase
#None
#Zero of any numeric type
#Any empty sequence. For example, '',(),[]
#Any empty mapping. For  example,{}.

condition = False

if condition:
    print('Evaluate to True')
else:
    print('Evaluated to Flase')
    
"""When condition is False, the if condition: part fails, 
and Python moves on to the else block, executing its content."""


### """******NOTE*****"""
 
# Python treats variables in a boolean context, 
"""it means that Python can automatically interpret certain types of values as 
either True or False without needing explicit comparison (like == True or == False).

In Python, some values are considered truthy (treated as True), 
and some are considered falsy (treated as False) when used in conditions 
like if, while, etc.
"""

# Examples of truthy values:
"""Any non-zero number (1, -5, 3.14, etc.)
Non-empty strings ("Hello", "False", etc.)
Non-empty lists, tuples, sets, dictionaries ([1, 2], (3, 4), {"key": "value"}, etc.)"""

# Examples of falsy values:
"""
0 (zero)
None (a special keyword representing "nothing")
False (the boolean False itself)
Empty collections (empty list [], empty tuple (), empty set set(), empty dictionary {} OR we can say empty mapping )
Empty strings ("")
"""

#Examples:

# Example in a boolean context:

logged_in = True

if logged_in:  # Python knows logged_in is True, so this block runs
    print("You're logged in!")
# This is equivalent to:
if logged_in == True:
    print("You're logged in!")
    
# But if logged_in: is cleaner.


# Similarly:

balance = 0

if not balance:  # Since balance is 0 (falsy), this condition is True
    print("No balance available.")
    
# How Python interprets common values:

if 42:  # Non-zero numbers are truthy
    print("This will print.")
    
if "":  # Empty strings are falsy
    print("This will not print.")
    
if []:  # Empty list is falsy
    print("This will not print.")
    
if [1, 2]:  # Non-empty list is truthy
    print("This will print.")
    
"""This is what we mean by Python treating values in a boolean context: it evaluates them 
as True or False based on their value, type, or content,
without needing explicit comparisons."""