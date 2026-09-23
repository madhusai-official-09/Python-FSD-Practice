# 1. Write a Python program using a for loop to print all numbers from 1 to N that have exactly 3 factors.
# Input:
# 30
# Output:
# 4 9 25
""" n = 30
for i in range(1,n+1):
    num = i
    count = 0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==3:
        print(num) """
            
# 2. Write a Python program using a for loop to print all numbers from 1 to N whose product of digits is an even number.
# Input:
# 25
# Output:
# 2 4 6 8 10 12 14 16 18 20 21 22 23 24 25

""" n = 25
for i in range(1,n+1):
    num = i
    p = 1
    while i>0:
        d = i%10
        p*=d
        i//=10
    if p%2==0:
        print(num) """
        
# 3. Write a Python program using a for loop to print all numbers from 1 to N that are divisible by the sum of their digits.
# Input:
# 30
# Output:
# 1 2 3 4 5 6 7 8 9 10 12 18 20 21 24 27 30

""" n = 30
for i in range(1,n+1):
    num = i
    s = 0
    while i>0:
        d=i%10
        s+=d
        i//=10
    if num%s==0:
        print(num) """
        
# 4. Write a Python program using nested for loops to print the following Continuous Alphabet Triangle Pattern.
# Input:
# 5
# Output:
# A
# BC
# DEF
# GHIJ
# KLMNO

""" rows = 5
count = 1
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(64+(count)),end="")
        count+=1
    print() """

# 5. Write a Python program using nested for loops to print the following Reverse Alphabet Triangle Pattern.
# Input:
# 5
# Output:
# ABCDE
# ABCD
# ABC
# AB
# A

""" rows = 5
for i in range(1,rows+1):
    for j in range(rows-i+1):
        print(chr(64+(j+1)),end="")
    print() """
    
# 6. Write a Python program using nested for loops to print the following Reverse Descending Alphabet Pattern.
# Input:
# 5
# Output:
# EDCBA
# EDCB
# EDC
# ED
# E

""" rows = 5
for i in range(1,rows+1):
    for j in range(1,rows-i+2):
        print(chr(64+rows-j+1),end="")
    print() """