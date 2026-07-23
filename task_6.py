# 1. Write a Python program to count the frequency of a given digit in a number using a while loop.
# Input:
# Number: 122313221
# Digit: 2
# Output: 4

""" num = int(input("Enter a Number: "))
digit = int(input("Enter Digit: "))
count = 0
while num>0:
    d = num%10
    if d == digit:
        count+=1
    num =num//10
print(count) """

# 2. Write a Python program to count how many even digits and odd digits are present in a given number using a while loop.
# Input: 4827316
# Output:
# Even digits: 4
# Odd digits: 3

""" num = 4827316
even = 0
odd = 0
while num>0:
    d = num%10
    if d%2==0:
        even+=1
    else:
        odd+=1
    num=num//10
print("Even digits->",even)
print("Odd digits->",odd) """

# 3. Write a Python program to reverse a number and check whether the reversed number is divisible by 11 using a while loop.
# Input: 121
# Output: Divisible by 11

""" num = 121
rev = 0
while num >0:
    d = num%10
    rev = rev*10+d
    num= num//10
if rev%11==0:
    print("Divisible by 11")
else:
    print("Not Divisible by 11") """
    
# 4. Write a Python program to find the sum of all even digits and the sum of all odd digits in a given number using a while loop.
# Input: 4827316
# Output:
# Sum of even digits: 20
# Sum of odd digits: 10

""" num = 4827316
even = 0
odd = 0
while num >0:
    d = num%10
    if d%2==0:
        even = even+d
    else:
        odd=odd+d
    num = num//10
print("Sum of even digits: ",even)    
print("Sum of odd digits: ",odd) """    

# 5. Write a Python program to count the number of digits that are greater than 5 in a given number using a while loop.
# Input: 58392716
# Output: 4

""" num = 58392716
digit = 5
count = 0
while num > 0:
    d = num%10
    if d>digit:
        count+=1
    num = num//10
print(count) """