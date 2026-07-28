# 1. Write a Python program using a for loop to print all even numbers from 1 to N.
# Input:
# 20
# Output:
# 2 4 6 8 10 12 14 16 18 20

""" n = 20
for i in range(2,n+1,2):
    print(i) """
    
# 2. Write a Python program using a for loop to print all Prime Numbers from 1 to N.
# Input:
# 30
# Output:
# 2 3 5 7 11 13 17 19 23 29

""" n = 30
for i in range(2,n+1):
    num = i
    count = 0
    for j in range(2,(num//2)+1):
        if num%j==0:
            count+=1
    if count == 0:
        print(num) """
        
# 3. Write a Python program using a for loop to print all Perfect Numbers from 1 to N.
# Input:
# 30
# Output:
# 6  28
# Explanation:
# A Perfect Number is a number that is equal to the sum of its proper divisors (excluding the number itself).

""" n = 30
for i in range(1,n+1):
    num = i
    s = 0
    for j in range(1,(num-1)+1):
        if num%j ==0:
            s+=j
    if num == s:
        print(num) """
        
# 4. Write a Python program using nested for loops to print the following Number Triangle Pattern.
# Input:
# 5
# Output:
# 1
# 12
# 123
# 1234
# 12345
 
""" row = 5
for row_cnt in  range(1,row+1):
    for row_no in range(1,row_cnt+1):
        print(row_no,end="")
    print() """
 
# 5. Write a Python program using nested for loops to print the following Repeated Number Pattern.
# Input:
# 5
# Output:
# 1
# 22
# 333
# 4444
# 55555

""" row = 5
for row_cnt in range(1,row+1):
    for row_no in range(1,row_cnt+1):
        print(row_cnt,end="")
    print() """
            
# 6. Write a Python program using nested for loops to print the following Right Angle Triangle Star Pattern.
# Input:
# 5
# Output:
# *
# **
# ***
# ****
# *****

""" row = 5
for row_cnt in range(1,row+1):
    print("*"*row_cnt,end="")
    print() """
    
    
    
        

