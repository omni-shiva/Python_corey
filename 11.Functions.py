def hello_func():
    print('Help Function!')

"""hello_func() # we need to add the (), in order to excecute the function, 
without (), hell0_func is equal to just the function itself like orignal def hello_func() and will not return/print anything unless ()"""

print(hello_func) # <function hello_func at 0x0000013149B7D080> so it  a function in certain location in memory .
hello_func() # Now that we are running the function with the print statement we dont need to print  it again.

#DRY CODE - Dont Repeat Yourself. Clean Code.

# RETURNING

def hello_func():
    return 'Hello Function'

print(hello_func().upper()) 

# So here as we are aware that hello_func() will return the string, so we can apply the string method on the top of that .


def hello_func(greeting): 
    return '{} Function.'.format(greeting)

print(hello_func('Hi')) 

'''This greeting variable doesn't affects any variables outside of the function,
its scope is only local to the function.'''

"""
THIS GREETING PARAMETER IS A REQUIRED ARGUMENT, IF WE DON'T HAVE A DEFAULT VALUE.
IF WE HAVE THAT , WHENEVER WE DIDN'T PASS THAT ARGUMENT IN.
"""



def hello_func(greeting,name = 'you'):  # here passed the default in name.
    return '{}, {}.'.format(greeting,name)

print(hello_func('Hi','Shiva'))

#Here  below once we have tuple and the dictionary , we can do whatever we want to.


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
    
courses = ['Math','Art']
info = {'name':'John','age':22}
    
student_info(*courses,**info) 
""" without */** , this basically giving the complete list and complete dictionary as positional argument , rather than seperate.
# So here basically * will unpack the list and ** will unpac the dictionary , 
# and pass it one by one, its same like - student_info(Math','Art',**info)"""


##*********EXAMPLES********####


#Number of days per month. First value palceholder for indexing purposes.

month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def is_leap(year):
    """Return True for leap years,False for non-leap years."""
    return year%4 == 0 and (year%100 != 0 or year % 400 == 0)

def days_in_month(year,month):
    """Return number of days in that month in that year"""
    
    if not 1 <=month <=12:
        return 'Invalid Month'
    
    if month==2 and is_leap(year):
        return 29
    return month_days[month]

a = days_in_month(2017,2)
print(a)