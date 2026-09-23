# 1. Write a Python program using a for loop to find the Largest Prime Factor of a given number.
# Input:
# 84
# Output:
# 7

""" n = 84
largest = 0
for i in range(1,n+1):
    if n%i==0:
        num =i
        count = 0
        for j in range(2,(num//2)+1):
            if num%j==0:
                count+=1
        if count==0:
            if num>largest:
                largest = num
print(largest) """

# 2. Write a Python program using a for loop to print all numbers from 1 to N whose last digit is a Prime Number (2, 3, 5, or 7).
# Input:
# 30
# Output:
# 2 3 5 7 12 13 15 17 22 23 25 27

""" n = 30
count = 0
for i in range(1,n+1):
    num = i
    last = num%10
    if (last==2 or last==3 or last==5 or last==7):
        print(i) """  
        
# 3. Write a Python program using a for loop to print all Perfect Square Numbers from 1 to N.
# Input:
# 50
# Output:
# 1 4 9 16 25 36 49
# Explanation:
# A Perfect Square Number is a number that can be expressed as the square of an integer.

""" n = 50
for i in range(1,n+1):
    for j in range(1,i+1):
        if j*j==i:
            print(i) """
# 4. Write a Python program using nested for loops to print the following Alphabet Triangle Pattern.
# Input:
# 5
# Output:
# A
# AB
# ABC
# ABCD
# ABCDE

""" rows = 5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(64+j),end = "")
    print() """
    
# 5. Write a Python program using nested for loops to print the following Repeated Alphabet Pattern.
# Input:
# 5
# Output:
# A
# BB
# CCC
# DDDD
# EEEEE

""" rows = 5
for i in range(1,rows+1):
    for j in range(1,i+1):
        print(chr(64+i),end="")
    print() """
    
# 6. Write a Python program using nested for loops to print the following Continuous Number Triangle Pattern.
# Input:
# 5
# Output:
# 1
# 23
# 456
# 78910
# 1112131415

""" rows = 5
n=1
for i in range(1,rows+1):
    for j in range(i):
        print(n,end="")
        n=n+1
    print() """

