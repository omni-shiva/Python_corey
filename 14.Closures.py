# Closures

""" A closure is a record storing a function together with an environment : a mapping associating each freee variable
of the function with the value or storage location to which the name was bound when the closure was created.
A closure , unlike a plain function , allows the funcitons to access those captured variables through the closure's 
reference to them, even when the functions is invoked outside their scope.
"""
# 1 .
def outer_func():
    message = 'Hi' 
    
    def inner_func():
        print(message) # message is  a free variable, as we actually didnt defined in the inner funciton - 
        # but we still have access to it within even after finish excecuting.
    return inner_func



my_func = outer_func() # here now my_func variable is a function now .
print(my_func.__name__)
my_func()
my_func()
my_func()

# 2 . outer_func with argument.

def outer_func(msg):
    message = msg 
    
    def inner_func():
        print(message) # message is  a free variable, as we actually didnt defined in the inner funciton - 
        # but we still have access to it within even after finish excecuting.
    return inner_func



my_func = outer_func('helloo') # here now my_func variable is a function now .
print(my_func.__name__)
my_func()
my_func()
my_func()

# A closure closes over the message variable from the enviorment.

####### Exampele #######
import logging
logging.basicConfig(filename='example.log',level = logging.INFO)

def logger(func):
    def log_func(*args):   #*args takes any number of arguments
        logging.info(
            'Running "{}" with arguments {}'.format(func.__name__,args)
            )
        print(func(*args)) # actually here we are excecuting the function(add,sub fun) with arguments .
    return log_func

def add(x,y):
    return x+y
def sub(x,y):
    return x-y
# So basically inner fun  named log_fun(*args) , executing the add and sub fun.
add_logger = logger(add)
sub_logger = logger(sub)

add_logger(3,3)
add_logger(44,5)




