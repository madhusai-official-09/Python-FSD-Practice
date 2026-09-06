# 1.Write a Python program to print all Disarium Numbers between 1 and N using a for 
# loop. 
# Input:100 
# Output:1 2 3 4 5 6 7 8 9 89 
# Explanation: Number in which the sum of its digits raised to the power of their 
# respective positions is equal to the number itself. 

""" n = 100
for i in range(1,n+1):
    num = i
    temp = i
    count = 0
    while i>0:
        i//=10
        count+=1
    d = 10**(count-1)
    power_cnt = 0
    s = 0
    while temp>0:
        digit = temp//d
        power_cnt+=1
        power=digit**power_cnt
        s+=power
        temp=temp%d
        d=d//10
    if s==num:
        print(num) """

# 2. Write a Python program to print all Harshad (Niven) Numbers between 1 and N using 
# afor loop. 
# Input:Enter N: 30 
# Output:1 2 3 4 5 6 7 8 9 10 12 18 20 21 24 27 30 

""" n = 30
for i in range(1,n+1):
    s = 0
    num = i
    while i>0:
        d = i%10
        s+=d
        i//=10
    if num%s==0:
        print(num) """

# 3. Write a Python program to print the following pattern using a for loop. 
# Input:Enter number of rows: 5 
# Output: 
# 15 14 13 12 11 
# 10  9  8  7 
# 6  5  4 
# 3  2 
# 1 

""" rows = 5
s = 0
for i in range(1,rows+1):
    s+=i
    num =s 
for i in range(1,rows+1):
    for j in range(1,rows-i+2):
        print(num,end=" ")
        num-=1
    print() """

# 4.write a python program to print the below pattern? 
# Input: n=5 
# Output: 
# A 
# B A 
# C B A 
# D C B A 
# E D C B A 

""" rows = 5
for i in range(1,rows+1):
    for j in range(i,0,-1):
        print(chr(64+j),end="")
    print() """
