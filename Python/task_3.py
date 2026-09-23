# 1.A movie theater has 20 seats. Seats with numbers divisible by 5 are reserved. Write a program to display only the available seat numbers?

# Input:20
# Output:1 2 3 4 6 7 8 9 11 12 13 14 16 17 18 19

""" seats = int(input("Enter Number of seats: "))
i = 1
while i<=seats:
    if i%5!=0:
        print(i)
    i+=1 """
    
# 2.A company issues employee IDs from 1001 to 1020. Write a program to count how many employee IDs are even?

# Output:10

# Explanation:
# Count the IDs that are divisible by 2.

""" id_start = 1001
id_end = 1020
count = 0
while id_start<=id_end:
    if id_start%2==0:
        count = count + 1
    id_start+=1
print(count) """

# 3.A game contains 15 levels. Bonus rewards are given for levels divisible by 3. Write a program to display all bonus levels?

# Input:15
# Output:3 6 9 12 15

# Explanation:
# Display levels that are divisible by 3.
    
""" levels = 15
i = 1
while i<=levels:
    if i%3==0:
        print(i)
    i+=1 """
    
# 4.A library contains books numbered from 1 to 50. Write a program to count how many book numbers are multiples of 7?

# Input:50
# Output:7

# Explanation:
# The book numbers are 7, 14, 21, 28, 35, 42 and 49.

""" books = 50
i = 1
while i<=books:
    if i%7==0:
        print(i)
    i+=1 """
    
# 5.Write a program to find the first number greater than 100 that is divisible by both 7 and 9 using a while loop?

# Output:126

# Explanation:
# Continue checking numbers until a number divisible by both 7 and 9 is found.

""" num = int(input("Enter a Number: "))
while True:
    if (num%7==0 and num%9==0) and (num>100):
        print(num)
        break
    num+=1 """

# 6.Write a program to print all numbers from 1 to n whose square is less than 50?

# Input:20
# Output:1 2 3 4 5 6 7
# Explanation:
# The squares of these numbers are less than 50.

""" num = 20
i = 1
while i <=num:
    sqr = i*i
    if sqr<50:
        print(i)
    i+=1 """

        
""" num = int(input("Enter a Number: "))
rev = 0
while num > 0:
    d = num%10
    rev = (rev*10)+ d
    num = num//10
org = 0
while rev > 0:
    d1 = rev%10
    org = (org*10) + d1
    rev = rev//10
print(org) """

num = int(input("Enter a Number:"))
h = 1
org = 0
i = 1
while i<=num:
    d = num//h
    h = h * 10
    org = org+d
    num = num%h
    i+=1
print(org)

        
