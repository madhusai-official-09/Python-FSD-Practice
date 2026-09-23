# 1. Write a Python program to check whether a given number is a Palindrome using a while loop.
# Input: 1221
# Output: Palindrome

""" num = 1221
bkp = num 
rev = 0
while num >0:
    d=num%10
    rev = rev*10+d
    num = num//10
if rev == bkp:
    print("Palindrome")
else:
    print("Not Palindrome") """
    
# 2. Write a Python program to repeatedly find the sum of the digits of a given number using a while loop until a single-digit number is obtained.
# Input: 4589
# Output: 8

""" num = 4589
s = 0
s1 = 0
while num>0:
    d = num%10
    s+=d
    num = num//10
while s>0:
    d = s%10
    s1+=d
    s = s//10
print(s1) """

# 3. Write a Python program to check whether a given number is an Armstrong Number using a while loop.
# Input: 153
# Output: Armstrong Number

""" num = 153
num1 = num
count = 0
while num>0:
    d = num%10
    num = num//10
    count+=1

s = 0
bkp = num1
while num1>0:
    d = num1%10
    d = d**count
    s+=d
    num1 = num1//10
if s == bkp:
    print("Armstrong")
else:
    print("Not Armstrong") """
    
# 4. Write a Python program to print the Fibonacci series up to n terms using a while loop.
# Input: 8
# Output:
# 0 1 1 2 3 5 8 13

""" n = 8
a = 0
b = 1
print(a,b,end=" ")
i = 0
while i<=n-2:
    c = a+b
    print(c,end = " ")
    a = b
    b = c
    i+=1 """
    
# 5. Write a Python program to check whether a given number is a Neon Number using a while loop.
# Input: 9
# Output: Neon Number

# Explanation:
# 9² = 81
# 8 + 1 = 9
# Since the sum of the digits of the square is equal to the original number, print Neon Number.

""" num = 9
square = num ** 2
s = 0
while square>0:
    d = square%10
    s+=d
    square//=10
if s == num:
    print("Neon Number")
else:
    print("Not Neon Number") """
    
    
num = int(input("Enter a Number: ")) #8853
largest = 0 # 3, 5, 8, 8
second = 0 # 3, 5, 8
third = 0 # 3, 5
fourth = 0 # 3
while num>0: #8853>0, 885, 88, 8
    d = num%10 #8853%10 -> d= 3, 5, 8, 8
    if d>=largest: #3>=0 -> T, 5>=3 -> T, 8>=5 -> T, 8>=8 -> T
        fourth = third # 0 = 0, 0 = 0, 0 = 0, fourth = 3
        third = second # 0 = 0, 0 = 0, third = 3 , third = 5
        second =largest # 0 = 0, second = 3, second = 5, second = 8
        largest = d # largest = 3, 5, 8, 8
    elif d>=second : 
        fourth = third
        third = second
        second = d
    elif d>=third :
        fourth = third
        third = d
    elif d>=fourth :
        fourth = d
    num=num//10 # 8853//10 = 885 , 88, 8
print(largest,second,third,fourth) 


    
      
    

    