#youtube link - https://www.youtube.com/watch?v=k9TUPpGqYTo
message = 'Hello World'
print(message.lower()) # all lower
print(message.upper()) # all upper
print(message.count('Hello')) # it takes string as an argument.
print(message.find('W')) #To find the index of certain charcater being used.
# If that doesnt exist it will return -1
message = message.replace('World','Universe') # WE NEED TO set a new variable here to get the updated return
print(message)

'''Concat and string ops and String Formating '''

greeting = 'hello'
name = 'Michael'

message = greeting + ', ' + name  + '. welcome!' #but it will not include space, so to that ' '
print(message)
#But the above method is not very efficient to use in long run.
"""SO better lets use formatted string.and use place holder {}"""
message = '{}, {}. Welcome!'.format(greeting,name) # best to use
print(message)

"""F STRINGS """
message = f'{greeting}, {name.upper()}. Welcome!' # best to use
print(message)
# BASICALLY in f-string we can also call string methods.

print(dir(name)) # it tell what class and methods available to us.










