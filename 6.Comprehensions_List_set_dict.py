#List Comprehension in python
'''
It is an easier and more readable way to create a list.
'''
num = [1,2,3,4,5,6,7,8,9,10]

# I Want 'n' for each 'n' in nums
my_list = []# Defining an empty list.
for n in num:
    my_list.append(n)
print(my_list)

my_list = [n**2 for n in num]
print(my_list) # so for each n in num. i want n**2 , this is what it means here.


"""
Using a map + lambda.
"""
'But problem is its unreadble and easy like list comprehensions'
#MAP - its basically run , everything in a list through certain funcitons.
#lambda : anonymus function.

num = [1,2,3,4,5,6,7,8,9,10]
my_list = map(lambda n: n*n*n, num)
print(list(my_list))

"""
The map() function returns a map object, which is an iterator.
This is why we're not seeing the result directly printed as a list. 
To actually see the list, you need to convert the map object to a list explicitly.
"""

##I Want 'n' for each 'n' in num if 'n' is even.
num = [1,2,3,4,5,6,7,8,9,10]
my_list = []
for n in num:
    if n%2 == 0:
        my_list.append(n)
        print('even\t',my_list)
print('final\t',my_list)

'Using List-Comprehensions'
num = [1,2,3,4,5,6,7,8,9,10]

my_list = [n for n in num if n%2 == 0]
print(my_list)

'Using a Fliter + Lambda'
num = [1,2,3,4,5,6,7,8,9,10]
my_list = filter(lambda n: n%2==0 , num )
print(my_list)

## I Want a (letter,num) pair for each letter in 'abcd' and each number in '0123'
#Like = A0,A1,A2,A3,B0,B1.......
'Using FOr loops'
num = [1,2,3,4,5,6,7,8,9,10]
my_list = []
for i in 'abcd':
    for n in range(4):
        my_list.append((i,n))
print(my_list)


'List Comprehension Method'
num = [1,2,3,4,5,6,7,8,9,10]
my_list = [(letter,num) for letter in 'abcd' for num in range(4)]
print(my_list)


# Dictionary Comprehensions.
name = ['Bruce','Clark','peter','Logan','Wade']
heros = ['Batman','Superman','Spiderman','Wolverine','Deadpool']

#I want a dict {'name':'heros'} for each name , hero in zip(names,heros)
my_dict = {}
for name,hero in zip(name,heros): 
    my_dict[name] = hero
print(my_dict)

#NOTE#
"""
this zip will give tuple.

for name, hero in zip(name, heros):
zip(name, heros): The zip() function takes two iterable objects (name and heros) and pairs their elements together. 
So, 
if name = ['Bruce', 'Clark'] and 
heros = ['Batman', 'Superman'], 
zip(name, heros) will produce 
an iterator that pairs corresponding elements, i.e., 
[('Bruce', 'Batman'), ('Clark', 'Superman')].

for name, hero in zip(...): This is a loop that iterates over the pairs of names and heroes produced by zip(). 
In each iteration:
name takes the value of the current element from the name list.
hero takes the value of the corresponding element from the heros list.

"""

############################
# my_dict[name] = hero
"""
This line adds a key-value pair to the dictionary:

name is used as the key, and hero is used as the value.
For example:

In the first iteration, my_dict['Bruce'] = 'Batman'.
In the second iteration, my_dict['Clark'] = 'Superman'.
This keeps adding more key-value pairs to the dictionary in each iteration."""

###############################
#_________________[concept]
""""
Let's clarify how Python distinguishes between a dictionary key-value pair assignment 
and a regular variable assignment, like when assigning a value in a column of a table.

Key Differences:

Dictionary Assignment:
my_dict[name] = hero is dictionary key-value assignment.
In this context, my_dict is a dictionary, and name is used as the key for storing a value (which is hero) in that dictionary.
Structure: A dictionary is always a collection of key-value pairs. 
That's why my_dict[name] = hero means name is the key, and hero is the value.

Column or Regular Assignment:
If my_dict were a list or other data structure, the interpretation could be different. 
For example, in a list, my_list[index] = value would be updating an element at a specific index,
which is akin to updating a "column" in a data frame.
"""
#########################

names = ['Bruce','Clark','peter','Logan','Wade']
heros = ['Batman','Superman','Spiderman','Wolverine','Deadpool']

# {} - For dictionary comprehension, we will use,{}

my_dict = {name:hero for name,hero in zip(names,heros)}
print(my_dict)

'IF name not equal to peter , say we are adding comprehension'
names = ['Bruce','Clark','Peter','Logan','Wade']
heros = ['Batman','Superman','Spiderman','Wolverine','Deadpool']

my_dict = {name:hero for name,hero in zip(names,heros) if name != 'Peter'}
print(my_dict)


### SET-COMPREHENSIONS ###

nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = set()
for n in nums:
    my_set.add(n)
print(my_set)

'in set comp'
nums = [1,1,2,1,3,4,3,4,5,5,6,7,8,7,9,9]
my_set = {n for n in nums}
print(my_set)

###############################################
'********COMPREHENSIONS ENDED*****************'
###############################################

#Genrator Expression.(SIMILAR TO LIST COMP)

#I want to yield 'n*n' for each 'n' in nums

nums = [1,2,3,4,5,6,7,8,9,10]

def gen_func(nums):
    for n in nums:
        yield n*n


my_gen = gen_func(nums)

for i in my_gen:
    print(i)

#### writing above in comp ###
nums = [1,2,3,4,5,6,7,8,9,10]
my_gen = (n*n for n in nums) # so () - represent generator
print('before i',my_gen)
for i in my_gen:
    print(i)