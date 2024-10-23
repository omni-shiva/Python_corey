'''
LEGB
Local, Enclosing, Global, Built-in
'''
# Local      - are variables defined within the function.
# Enclosing  - Enclosing are variables in the local scope of enclosing/nested functions.
# Global     - Globals are the variables defined at the top level of a module or explicitly declared Global using  the global keyword.
# Built-in   - Builts-ins are just names that are preassingned in python.

'''THIS ORDER LEGB , is very imp as this is the order that determines what a variable is assigned to so python first check the variables
in the local scope then the enclosing scope then the global and then lastly the built-ins.'''

####*****GLOBAL AND LOCAL SCOPE *****####

x = 'global x' #here x is global variable as it is in the MAIN BODY , of our file .

def test():
    # global x # if we want that local x below to effect the outside global x. we should not over use it.
    # , we need to mention that global x , and this will work even if x = 'global x' , not defined outside.
    x = 'local x'   #Now this y variable here is local variable and local to the test function.
    # print(y)
    print(x)


test() # here python use that LEGB rule and print out the y variable first ,that is with in test()
print(x) # If we do this, it will give error as this y variable  is LOCAL. so its unable to find LEGB out side. so name error.


def test(z):
    x = 'local x'
    print(z)
    
test('local z') # here we are give argument , local z that is being passed to test(z), then which is printing z.

##### Built-In functions #########

import builtins

# IF WE LIKE TO VIEW THE VARIABLES IN THE BUILT IN SCOPE.
print(dir(builtins)) # THIS dir() -  get the list of the attribute of the given obejct , here i.e builtins.



m = min([5,1,4,2,3]) # it will work like this ,as buit in  but say below , if we define min() func.
print(m)

############
def min():
    pass


m = min([5,1,4,2,3])
"""now it will give error, bcz of the min() takes 0 positional arguments but 1 was given. 
this error happened bcz  when we ran this Min funciton here,python fuction found our Min function in the global scope , before it 
fell back to built in scope. 
"""
print(m)

# Now this will work , min will directy go to the builtin function rather than global one.

def my_min():
    pass

m = min([5,1,4,2,3])
print(m)

##*******ENCLOSING - FUNCTION**********##


x = 'global x'

def outer():
    x = 'outer x' # if it commented out , then now print(x) below will give error , as it has no enclosing outer function to check for x.
    
    def inner():
        # x = 'inner x' # Follow LEGB and as L - local , not here, 
        # it will go to enclosing function to checking for x i.e outer x. and it will print the same . so it ENCLOSING SCOPE.
        print(x)
    inner()
    print(x)

outer()



