'**Dictionaries**'
#############################
"""This allows us to work with key value pair, 
where key is the unqiue indentifier of data and Value is that data """


student = {1:'John','age':25,'courses':['Math','CompSci']}
print(student)

'Keys can be any immutable data type . string or intergers or others.'

print(student[1]) # here key value pair is not indexing.
print(student['phone']) # error for non existent key.
#Say if we dont want error if any key there or not , if not it should give None  ,then->>
print(student.get('phone')) # Now it will give None.
'To get Default value if that key not found '
print(student.get('phone','Not Found')) # 2nd arg except default value , if None.


'''ADDING NEW KEY OR UPDATING THE EXISTING'''
student = {'name':'John','age':25,'courses':['Math','CompSci']}
student['phone'] = '555-5555' # here NEW KEY ADDED AND value
student['name'] = 'Jane' # here value updated as the key already exist.
print(student)

#UPDATE - 
'This basically helps in creating the Multiple Update in one go'
student = {'name':'John','age':25,'courses':['Math','CompSci']}
student.update({'name':'Jane','age':26,'phone':'555-5555'})
print(student)


"""Deleting the Specific Key and its value"""
student = {'name':'John','age':25,'courses':['Math','CompSci']}
#Using DEL keyword.
del student['age']
print(student)

#Using POP.

student = {'name':'John','age':25,'courses':['Math','CompSci']}
#POP method will remove but also return that value , we need to assign it and store it to print

age = student.pop('age')
print(student) # This will  be without age.
print(age) # Here the stored poped vlaue, so now we got the both value, removed one and final one.


"""Loop Through Dictionary"""
student = {'name':'John','age':25,'courses':['Math','CompSci']}
print(len(student)) # Length=3 means , we have 3 keys in dict.

print(student.keys()) # It will give all the keys list.
print(student.values()) # it will give values only .
print(student.items()) #IT WILL GIVE the combo of key value pair
print(student)

for key in student:
    print(key)
    
    
#IF WE WANT KEY,VALUE PAIR in loop/
for key,value in student.items():
    print(key,value)