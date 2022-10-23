# while loop
i = 1

while i < 11:
    print (i)
    i += 1


# printing a pattern
row =6
for i in range (1,row + 1):
    for j in range(1, i+1):
        print (j, end=" ")

    print(" ")


    
# find the sum of a number and it's average
num = int(input('Enter a number:'))
sum = 0

for num in range (1, num-3):
    sum = sum + num
print("The sum of the first", num, "numbers is:", sum)
average = num / 2
print("The average of the first", num, "numbers is:", average)


from ast import Num
from lib2to3.pgen2.token import NUMBER

# print a multiplication table
num = 2

for i in range(1, 11):
    n = num * i
    print (n)


# Write a program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for n in numbers:
    if n > 500:
        break
    if n > 150:
        continue
    if n % 5 == 0:
        print(n)

# Write a program to count the total number of digits in a number using a while loop.

num = 234566
count = 0

while num != 0: #while doing the floor division,once it is equal to 0 we stop
    num = num // 10 # / /10 is to reduce to last digit and throw away the remainder so we keep counting till we get to the end
    count += 1
print(count)
    

# write a program to use for loop to print the following reverse number pattern



list1 = [10, 20, 30, 40, 50]

size = len(list1) -1
for num in range(size, -1, -1):
    print(list1[num])
    