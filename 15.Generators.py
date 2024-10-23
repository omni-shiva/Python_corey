#Generators - It doesn't hold the entire result in memory it yield one result at a time and wait for us to ask for next result.
def square_numbers(num):
    for i in num:
        yield (i*i) #This yield show the generator object.

my_nums = square_numbers([1,2,3,4,5])


# print(my_nums)
# o/p -  <generator object square_numbers at 0x00000291B7E79490> # THIS SHOWS that its not  stored in memo and yiled one result at a time.

#So it will work like this 

# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))
# print(next(my_nums))

#But the good way to do it is , by for loop:

for num in my_nums:
    print(num)
    
####ALL ABOVE LINE OF CODE CAN BE WRITTEN BY LIST COMPREHENSION######
my_nums = [x*x for x in [1,2,3,4,5]]
print(my_nums)

# THE SAME way we can create generators by repalcing [] with ().

my_nums = (x*x for x in [1,2,3,4,5])
print(my_nums) # Here we see it gave one by one , as generator .

for num in my_nums:
    print(num)
    
#Now without loop also , we can convert the genrator object to list and store it in memory , as generator dont

my_nums = (x*x for x in [1,2,3,4,5])

print(list(my_nums)) # While doing this conversion generator to list conversion, we loosed the advantange of performance.
"""So a generator is better with performance, as it give one by one and doesnt store data in memory , 
while using it in 1000s-millions of row.
"""
"""so we dont get that issue with that generator as it doesn't store the value ,, to cause high memory usage."""


