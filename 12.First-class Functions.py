#First-Class Functions:
"In programming, a language is said to have First-Class Functions if it treats Functions as First-Class-Citizens."

# 1 . First Class Citizen(Programming):
"""A first-class citizen(sometimes called first class obejcts) in a programming language is an entity which supports all the 
operations generally available to the other entities. These operations typically include being passed as an argument ,
returned from  a function, and assigned to a variable """


def square(x):
    return x*x

# f = square(5) 
"""Here parenthesis () means we are gona execute the function. so we if we set like this""" 
f = square  
"""here its like we can treat the variable f like function , this is what called first class function"""

print(square)
print(f(5)) # 1. Assinging a function to a variable . ( first class fun)

# 2 . Higher order functions
"""we can also pass function as variables and returns functions as a result of other functions , so If A fuction accepts other fuctions
as arguments or returns functions as their results, that what we called HOF.
"""

# 2 . 1 Passing a fuction as an arguments to another function

def square(x):
    return x*x

def cube(x):
    return x*x*x

def my_map(func,arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result

squares = my_map(cube,[1,2,3,4,5]) # we are not adding the () to the square function , bcz it will execute the function.

print(squares)

# 3. Return a function from another fuction.

def logger(msg):
    
    def log_message():
        print('Log:',msg)
    return log_message  # here returning log_message func from logger func

log_hi = logger('Hi ! Shiva')
log_hi()

# More example

def html_tag(tag):
    
    def wrap_text(msg):
        print('<{0}>{1}</{0}>'.format(tag,msg))
    
    return wrap_text

print_h1 = html_tag('h1')
print_h1('Test Headline!')
print_h1('Another Headline!')

print_p = html_tag('p')
print_p('Test_paragraph !')

print(print_h1)