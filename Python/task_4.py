# 1. Write a Python program to count the number of even digits in a given number.
# Input: 4827316
# Output: 4

""" num = 4827316
count = 0
while num>0:
    d = num%10
    if d%2==0:
        count+=1
    num = num//10
print(count) """

# 2. Write a Python program to print the numbers from 1 to 100 that are prime numbers.
# Output: 2, 3, 5, 7, 11, ..., 97

""" num = 2
while num<=100:
    d = 2
    while d<=num//2:
        if num%d==0:
            break
        d+=1
    else:
        print(num)
    num+=1 """
    
# 3. Write a Python program to reverse the digits of a given number.
# Input: 3742
# Output: 2473

""" num = 3742
rev=0
while num>0:
    d = num%10
    rev = (rev*10) + d
    num = num//10
print(rev) """

# 4. Write a Python program to find the largest digit in the given number.
# Input: 23451678
# Output: 8

""" num = 23451678
count = 0
while num>0:
    d = num%10
    if d>count:
        count = d
    num=num//10
print(count)     """

# 5. Write a Python program to check whether a number is a Spy Number using a while loop.
# Input: 123
# Output: Spy Number

# Explanation:
# For 123
# Sum = 1 + 2 + 3 = 6
# Product = 1 × 2 × 3 = 6

""" num = 123
s = 0
p = 1
while num >0:
    d = num%10
    p= p*d
    s = s + d
    num = num//10
if s == p:
    print("Spy Number")
else:
    print("Not spy Number") """