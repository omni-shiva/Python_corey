person = {'name':'Jenn','age':23}

#Conventional String Formating
sentence = 'My name is ' + person['name'] + ' and I am ' + str(person['age']) + ' years old.' # type: ignore
print(sentence)


# These {} here are placeholders.
sentence = 'My name is {} and I am {} years old.'.format(person['name'],str(person['age'])) # type: ignore
print(sentence)


# We can explicity mention the place holders.
'It is most used full when this , same value and palce holder being repeated'
sentence = 'My name is {0} and I am {1} years old.'.format(person['name'],str(person['age'])) # type: ignore
print(sentence)

tag = 'hi'
text = 'This is a headline'

sentence = '<{0}>{1}</{0}>'.format(tag,text)
print(sentence)

#We can also directly call method in place holder, like we are calling directionary methods/LIST and attributes.
person = {'name':'Jenn','age':23}
sentence = 'My name is {0[name]} and I am {0[age]} years old.'.format(person) #**NOTE**###
print(sentence)

#Calling attribute like above.

class person():
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
p1 = person('shiva',26)

# SO BELOW instead of braces like 0[], we are simply using .attribute to grab the value.
sentence = 'My name is {0.name} and I am {0.age} years old.'.format(p1)
print(sentence)


#Passing Keyword argument to a format.
person = {'name':'Jenn','age':23}
sentence = 'My name is {name} and I am {age} years old.'.format(name = 'Jenn',age = '30')
print(sentence)

# Unpacking list/dict and using as keyword argument for formatting.
# 'This is the best method to print out dictionary'
'**kwargs used to unpack keywords , like dict. And *args used to unpack list or normal values.'

person = {'name':'Jenn','age':23}
sentence = 'My name is {name} and I am {age} years old.'.format(**person) #here it will unpack the full dictionary 
print(sentence)


# Formating in Numbers and Int.
for i in range(1,101):
    sentence = 'This value is {:02}'.format(i)
    print(sentence)
    
'This 0:2 means number passing will total 2 digit if there are single digit pad 0 before that.'

#Format for decimat Places.
pi = 3.14159265
sentence = 'Pi is equal to {:.2f}'.format(pi)
print(sentence)

#:.2f means2 decimal palce formating upto 2 digit


#Large number Comma sep formating 
'Say we want 1MB, 1000000 bytes, to show it properly in 1,000,000.00'

sentence = '1 MB is equal to {:,.2f}  bytes.'.format(1000**2)
print(sentence)

""" : This colon used to specify the formating and then , to say we want to seperate by comma."""


###########NOTE######
"FORMATING DATE TIME"
######################

import datetime
my_date = datetime.datetime(2016,3,1,12,30,45)
print(my_date)

# March 01,2016

sentence = '{:%B %d, %Y}'.format(my_date) #Refer datetime for the %B/D/d THINGS.
print(sentence)


"""March 01,2016 fells on a Tuesday and was the  061 day of the year."""
import datetime
my_date = datetime.datetime(2016,3,1,12,30,45)
sentence = '{0:%B %d, %Y} fells on a {0:%A} and was the {0:%j} day of the year.'.format(my_date)
print(sentence)