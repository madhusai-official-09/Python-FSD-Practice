# 1. Write a Python program to check whether a given number is a perfect cube or not.
# Input:27
# Output: Perfect Cube

""" num = int(input("Enter a Number: ")) 
root=1
while root**3<=num: 
    if root**3 == num: 
        print("Perfect cube")
        break
    root = root+1
else:
    print("Not a perfect cube") """
    
# 2. Write a program to calculate the factorial of a number using a while loop.
# Input:
# 5
# Output:
# 120

""" num = int(input("Enter a Number: "))
b=1
count = 1
while b<=num:
    count *= b
    b+=1
print(count) """

# 3. Write a program to count how many numbers between 1 and n are greater than 20.
# Input:
# 25
# Output:
# 5
# Explanation:
# The numbers are 21, 22, 23, 24, and 25.

""" num1 = 1
n = int(input("Enter a Number: "))
while num1<=n:
    if num1>20:
        print(num1)
    num1+=1 """

# 4. Write a program to print all numbers between 1 and n except multiples of 5.
# Input:
# 15
# Output:
# 1 2 3 4 6 7 8 9 11 12 13 14

""" num = int(input("Enter a Number: "))
i = 1
while i<=num:
    if i%5!=0:
        print(i)
    i+=1  """
    
# 5. Write a program to find the sum of numbers that are divisible by 4 between 1 and n.
# Input:
# 12
# Output:
# 24

""" num = int(input("Enter a Number: "))
i = 1
sum = 0
while i <= num:
    if i%4==0:
        sum+=i
    i +=1 
print(sum) """

# 6. Write a Python program to print all Prime Numbers from 1 to N using nested while loops.
# Input: 50
# Output: 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47
""" n=int(input("Enter a Number: "))
num = 2
while num <= n:
    d = 2
    while d<=num//2:
        if num%d==0:
            break
        d+=1
    else:
        print("Prime ->", num)
    num+=1 """
    
# 7. Write a Python program to print all the factors of a given number using a while loop.
# Input: 24
# Output: 1 2 3 4 6 8 12 24

""" num = int(input("Enter a Number: "))
i = 1
while i<=num:
    if num%i==0:
        print(i)
    i+=1 """
    
# 8. Write a Python program to find the sum of all factors of a given number.
# Input: 12
# Output: 28

""" num = int(input("Enter a Number: "))
i = 1
sum = 0
while i<=num:
    if num%i == 0:
        sum+=i
    i+=1
print(sum)   """  


