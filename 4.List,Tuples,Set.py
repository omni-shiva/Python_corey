#################################################
"""'''***********  LIST  ******************'''"""
#################################################
courses = ['History','Math','Physics','CompSci']

print(courses)
print(len(courses)) #This shows number of values in the list.
print(courses[3])  
print(courses[-1]) #-1 means always be the  last item of list.

print(courses[0:2])  # First index inclusive and 2nd index exclusive.
print(courses[:2])   # THIS WILL TAKEN FROM BEGINING 
print(courses[2:])

"""List Methods"""
"Adding values the list above , below are few methds."
courses.append('Art') #1. APPEND
print(courses)

# courses.insert(location_wr_we_waana_insert,value)

courses.insert(0,'Art') # it will only insert the value at 0th index without checking any dups or anything.
print(courses)

# Extend - We use this when we have multiple values to add to it.

courses = ['History','Math','Physics','CompSci']
courses_2 = ['Art','Education']

courses.insert(0,courses_2) # This insert will just insert the entrie list .
# "Like this - [['Art', 'Education'], 'History', 'Math', 'Physics', 'CompSci'] " # its a list of list.

courses.append(courses_2) # this also give list of list from the end.

# """# Extend takes only one argument.And it will not give list of list like insert and append , but it will just add the element in the list."""
courses.extend(courses_2)   

"""Removing Values from the List."""
courses = ['History','Math','Physics','CompSci']
# courses.remove('Math')
pooped = courses.pop() # BY Default it will remove last value of the list.
# pop will be helpfull if we waana use the list as stack or queue.
# Pop returns the value its removed.
print(pooped)
print(courses)

"""Reversing of list"""
courses = ['History','Math','Physics','CompSci']
courses.reverse()
print(courses)

"""Sorting the list , its alwats happen in ascending"""
courses = ['History','Math','Physics','CompSci']
courses.sort()
print(courses)

nums = [1,5,6,3,4]

nums.sort()
print(nums)

"Whatif we want it in decending"
nums = [1,5,6,3,4]
courses = ['History','Math','Physics','CompSci']
courses.sort(reverse=True)
nums.sort(reverse=True)
nums

"""*******Built-in List Functions """
# Sorted function we can use.
"""Whatif we want reverse without alterning the orginal list"""
courses = ['History','Math','Physics','CompSci']
sorted_courses =  sorted(courses) # using function and storing is the best way to use the list , if we dont waana change the orignal one.
print(sorted_courses)

"List of functions"
nums = [1,5,6,3,4]

print(min(nums))
print(max(nums))
print(sum(nums))

"""Indexing in List """

courses = ['History','Math','Physics','CompSci']

print(courses.index('CompSci'))  # 3 IT WILL GIVE

'Lets say when we are not sure if that value exist in list or not to get index then--'

print('Art' in courses ) # it give false.

print('Math' in courses )


"""Looping in list"""
for index,item in enumerate(courses,start=1):  
    #this enumerate function returns 2 values , it returns the index that were on and the value .
    print(index,item)
    
# iF we need above in tuple format then ,we just need to do this,
for item in enumerate(courses):
    print(item)


"""String Method Join and **Splitting** """

courses = ['History','Math','Physics','CompSci']

courses_str = ','.join(courses) #it will give comma sep values , withtout list in joining .

new_list = courses_str.split(',')
print(courses_str)
print(new_list)

'''list end'''

#################################################
"""'''***********TUPLES******************'''"""
#################################################

"""Lists a mutable but Tuples are not , they are immutable"""

"""if WE NEED SOMETHING THAT CAN BE MODIFY USE LIST , 
IF WE NEED SOMETHING THAT CAN LOOP THROUGH AND ACCESS USE tuple
"""
#Mutable

list_1 = ['History','Math','Physics','CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0]='Art'

print(list_1)
print(list_2)


#Immutable

tuple_1 = ('History','Math','Physics','CompSci')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

tuple_1[0] = 'Art' # Tuple doesnt support item assignment.

print(tuple_1)
print(tuple_2)

tuple_1[0] # We can access value and loop through , but we cant append, remove or any mutable sutff.



'Tuples End'
#################################################
"""'''***********SETS******************'''"""
#################################################

"Sets are Unordered and also have no Duplicates"

cs_courses =  {'History','Math','Physics','CompSci','Math'}
print(cs_courses)

#Use of set mostily is to check if a value belong to that set called 'Membership Test'. 
# And 2nd mostly used to remove duplicates.


#Membership Test.
print('Math' in cs_courses)  # this list and tuples also do , but sets are optimised to this.

'Set can also quickly do is checking either they share or dont share any value with other set'

cs_courses =  {'History','Math','Physics','CompSci','Math'}
art_course = {'History','Math','Art','Design'}


'What courses these set have comman in them ?'

print(cs_courses.intersection(art_course))

'What courses are in cs_courses but not in arts courses ?'

print(cs_courses.difference(art_course))

'All Courses offered in both set'

print(cs_courses.union(art_course)) # It will always give unqiue values.

'**Note**' # - For these above particular performance , sets are more performant than list or tuples.

"""
The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
"""
cs_courses =  {'History','Math','Physics','CompSci','Math'}
art_course = {'History','Math','Art','Design'}
print(cs_courses.symmetric_difference(art_course))


"Sets ENd"

#################################
#################################
'NOTES -'
#Empty List 

empty_list = []
'OR'
empty_list = list()

#Empty Tuples

empty_tuples = ()
'OR'
empty_tuples = tuple()

#Empty Sets

empty_set = {} #This isnt right! It's a empty dict.
empty_set = set() #only use built-in.

