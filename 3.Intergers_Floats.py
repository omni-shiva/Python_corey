num = 3.14
"""Python has a built in function called type 
where we can see the datatype of an obeject..
"""

"""Arithmetic OPs"""
print(type(num))

print(3//2) # Floor division

print(3**2) # Exponents

print(3%2)  #it will give remainder of division

"""Order of operations"""

print(3*2+1) #same as BODMAS

"""Incrementing a Variable"""

num = 1
num += 1 # its equal to num =  num+1
num *=10 # its equal to num =  num*10

print(num)

"""Absolute and Round"""
print(abs(-3)) # it wil give + ve

print(round(3.75,0)) # 0,1,2 indicate upto how many digit we want to be rounded off

"""Comparisons"""
# Equal:  3==2 
# Not Equal  3!=2
# Greater Than 3>2
# Less than   3<2
# greater or Equal  3>=2
# less or  Equal   3<=2


num_1 = 3
num_2 = 2

print(num_1==num_2)



"""Casting"""

num_1 = '100'
num_2 = '200'

num_1 = int(num_1)
num_2 = int(num_2)

print(num_1+num_2) # it just concat ,, as its work as string , if not converted to int

