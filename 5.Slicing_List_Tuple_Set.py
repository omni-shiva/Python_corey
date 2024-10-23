#####*****LIST SLICING******##**
my_list = [0,1,2,3,4,5,6,7,8,9]
#          0,1,2,3,4,5,6,7,8,9 - index
#         -10,-9,-8,-7,-6,-5,-4,-3,-2,-1  - negative index.

# print(my_list[-10])
#   list[start:end:step]
print(my_list[3:8])
print(my_list[-7:-2])
#Mixing Positive and negative.
print(my_list[1:-2])  # FROM 1 TO  -2 index i.e 8
print(my_list[1:]) #  1 to END
print(my_list[:-1])
print(my_list[:]) # it GIVE END TO END VALUE , as same as copy of orignal list.

#Step - allows us to skip the certain number of values.
my_list = [0,1,2,3,4,5,6,7,8,9]
print(my_list[2:-1:2]) # step = , print every 2nd value.
print(my_list[2:-1:-1]) # empty list , bcz there is noway it will go from 2 to 8 by doing negative step.
print(my_list[-1:2:-1])  # - 1 is must even if step  = 1 , bcz then only it will understand that we have minus the index, till 2

#Reversing the LIst AND Adv slicing.
my_list = [0,1,2,3,4,5,6,7,8,9]
print(my_list[::-1])
print(my_list[:2:-1])
print(my_list[:3:-1])

########################
#   STRING SLICING  
########################
sample_url = 'http://coreyms.com'
print(sample_url)

#Reverse the URL.
print(sample_url[::-1])

# get Top level domain(.com)
print(sample_url[-4:]) #even starting from -4 , our step is positive as we are going right side.

#   # Print the URL without the beginning htpp://
print(sample_url[7:])


# # print the url without the http:// or the top level domain.

print(sample_url[7:-4])