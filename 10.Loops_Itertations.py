nums = [1,2,3,4,5]


for num in nums:
    print(num)
    
    
    
# Break - This keyword, will completely break out of a loop.
#Continue - it moves on to the next iteration of the loop.
nums = [1,2,3,4,5]

for num in nums:
    if num == 3:
        print('Found!',num)
        break
    print(num)


 
for num in nums:
    if num == 3:
        print('Found!',num)
        continue
    print(num)
    

# loop with in loop
nums = [1,2,3,4,5]

for num in nums:
    for letter in 'abc': # SO what will happen here is for each num, letter will see each char of abc.
        print(num,letter)
print('outter')


#Range
# range(10) means 0 to 9
for i in range(1,11):
    print(i)
    
    
#While
x=0

while x<10: #it will run untill its true.
    if x==5:
        break
    print(x)
    x += 1
    
while True: #it will go infinite loop and will not break unless we do put break .
    if x==5:
        break
    print(x)
    x += 1
    
