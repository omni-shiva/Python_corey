"""Decorators - The one of the most used case for this in python is logging.
    Also timing how long functions run.
"""

def decorator_function(original_funciton):
    def wrapper_function(*args,**kwargs):
        print('wrapper executed this before {}'.format(original_funciton.__name__))
        return original_funciton(*args,**kwargs)
    return wrapper_function

"""Example 1 ."""
@decorator_function  # this is same as 
                     #decorator_display = decorator_function(display) AND decorator_display()
def display():
    print('display function ran')
    
# decorator_display = decorator_function(display)
# decorator_display()  
# this execute the wrapper function which then execute the wrapper function.

# display() 

#Note - This will not work here , when orignal function here take any argument.


@decorator_function
def display_info(name,age):
    print('display_info ran with arguments ({},{})'.format(name,age))
    
display()
display_info('John',25)



"""Example 2 ."""
"""With Class Decorator."""
class decorator_class(object):
    def __init__(self,orignal_function):
        self.original_function = orignal_function
    
    def __call__(self,*args,**kwargs):
        print('call method executed this before {}'.format(self.original_function.__name__))
        return self.original_function(*args, **kwargs)





@decorator_class
def display():
    print('display function ran')
    


@decorator_class
def display_info(name,age):
    print('display_info ran with arguments ({},{})'.format(name,age))
    
display()
display_info('John',25)


"""Example 3 ."""
"""Practical Example"""

from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__),level=logging.INFO)
    
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info('Ran with args: {}, and kwargs: {}'.format(args,kwargs))
        return orig_func(*args,**kwargs) # excueting the orig function  and returning the result,
    return wrapper

def my_timer(orig_func):
    import time
    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time() # take the current time
        result = orig_func(*args, **kwargs)
        t2 = time.time()-t1
        print('{} ran in: {} sec'.format(orig_func.__name__,t2))
        return result
    
    return wrapper


# @decorator_function
# def display():
#     print('display function ran')

    
import time

# Testing 
# display_info = my_timer(display_info)
# print(display_info.__name__)

"""Decorator Together"""

@my_logger
@my_timer# this lower one will execute first then above my timer 
# """Its same as  display_info = my_logger(my_timer(display_info))"""
def display_info(name,age):
    time.sleep(1)
    print('display_info ran with arguments ({},{})'.format(name,age))

display_info('withwrap',30)






        


































