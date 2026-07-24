# 1. Write a Python program to count how many digits in a given number are multiples of 3 using a while loop.
# Input: 9362481
# Output: 4

""" num = 9362481
count = 0
while num>0:
    d = num%10
    if d%3==0:
        count+=1
    num//=10
print(count) """

# 2. Write a Python program to check whether the first digit of a number is equal to the last digit using a while loop.
# Input: 74547
# Output: 

""" num = 74547
bkp = num
count= 1
while num>0:
    num=num//10
    count=count*10
div=count//10
num=bkp//div
second = bkp%10
if num==second:
    print("Yes")
else:
    print("No") """
    
# 3. Write a Python program to print the following square pattern.
# Input: 5
# Output:

# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *

""" rows = 5
row_cnt = 1

while row_cnt<=rows:
    print("* "*rows)
    row_cnt+=1 """ 

# 4. Write a Python program to print the following pattern.
# Input: 5
# Output:

# ****
# ***
# **
# *
""" rows = 5
row_cnt = 1
while row_cnt<=rows:
    print("*"*(rows-row_cnt+1))
    row_cnt+=1 """

# 5. Write a Python program to print all numbers between 1 and N whose sum of digits is even using a while loop.
# Input: 20
# Output:
# 2 4 6 8 11 13 15 17 19 20

""" num = 1
n = 20
while num<=n:
    if num<=9:
        if num%2==0:
            print(num)
    else:
        temp = num
        sum = 0
        while temp>0:
            d = temp%10
            sum+=d
            temp//=10
        if sum%2==0:
            print(num)                
    num+=1 """
    