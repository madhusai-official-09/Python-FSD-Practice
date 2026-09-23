# 1. Write a Python program using a while loop to find the Least Common Multiple (LCM) of two given numbers.
# Input: 12 18
# Output: 36
# Explanation:
# The Least Common Multiple (LCM) is the smallest positive number that is exactly divisible by both given numbers.

""" num1 = 12
num2 = 18
i = 1
while True:
    if i%num1==0 and i%num2==0:
        print(i)
        break
    i+=1 """

# 2. Write a Python program using a while loop to check whether a given number is a Happy Number or not.
# Input: 19
# Output: Happy Number
# Explanation:
# 19 → 1² + 9² = 82
# 82 → 8² + 2² = 68
# 68 → 6² + 8² = 100
# 100 → 1² + 0² + 0² = 1  ,Since the process reaches 1, the number is called a Happy Number.

""" num = 19
while True:
    sqr = 0
    while num>0:
        d = num%10
        sqr = sqr + (d**2)
        num//=10
    if sqr == 1:
        print("Happy Number")
        break
    else:
        num = sqr """
        
        
# 3. Write a Python program to print the following Hollow Right Triangle Star Pattern.
# Input: 5
# Output:
# *
# **
# * *
# *  *
# *****

""" rows = 5
row_cnt = 1
while row_cnt<=rows:
    if row_cnt==1 or row_cnt==rows:
        print("*"*row_cnt)
    else:
        print("*"," "*(row_cnt-rows//2),"*",sep="")
    row_cnt+=1 """
    
# 4. Write a Python program to print the following Right Pascal Star Pattern.
# Input: 5
# Output:
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

""" rows = 5
row_cnt = 1
while row_cnt<=rows*2:
    if row_cnt>= rows:
        print("*"*(rows -(row_cnt-rows)))
    else:
        print("*"*row_cnt)
    row_cnt+=1
 """
    
# 5.print the below pattern
# input: n=5
# output:
# *****
# *   *
# *****
# *   *
# *****

""" rows = 7
row_cnt = 1
while row_cnt<=rows:
    if row_cnt%2!=0:
        print("*"*rows)
    else:
        print("*"," "*(rows-2),"*",sep="")
    row_cnt+=1 """





    
    
    
    
    

