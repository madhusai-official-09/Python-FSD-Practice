# 1. Write a Python program to find the largest element in a given list.
# Input:
# [12, 45, 7, 89, 23]
# Output:
# 89

""" li = [12, 45, 7, 89, 23]
largest = 0
for i in li:
    if i>largest:
        largest = i
print(largest) """

# 2. Write a Python program to print all the elements present at even indices of a given list.
# Input:
# [10, 20, 30, 40, 50, 60, 70]
# Output:
# [10, 30, 50, 70]

""" li = [10, 20, 30, 40, 50, 60, 70]
n_li=[]
for i in li:
    idx = li.index(i)
    if idx%2==0:
        n_li.append(i)
print(n_li) """
        
# 3. Write a Python program to find the sum of all elements in a given list.
# Input:
# [5, 10, 15, 20]
# Output:
# 50

""" li = [5, 10, 15, 20]
s = 0
for i in li:
    s+=i
print(s) """

# 4. Write a Python program to create a new list containing only the numbers whose sum of factors is a Prime Number.
# Input:
# [9, 16, 20, 25]
# Output:
# [9, 16, 25]

""" li = [9, 16, 20, 25]
n_li=[]
for i in li:
    sum = 0
    for j in range(1,i+1):
        if i%j==0:
            sum+=j
    count=0
    for n in range(1,sum+1):
        if sum%n==0:
            count+=1
    if count==2:
        n_li.append(i)
print(n_li) """

# 5. Write a Python program to create a new list containing only the numbers for which the sum of the number and its reverse is a Palindrome Number.
# Input:
# [12, 15, 19, 23, 28]
# Output:
# [12, 15, 23]

""" li = [12, 15, 19, 23, 28]
n_li = []

for i in li:
    num = i
    sum =0
    while num>0:
        d = num%10
        sum+=d
        num//=10
    rev = 0
    bkp = sum
    while sum>0:
        d1 = sum%10
        rev = rev*10+d1
        sum//=10
    if rev==bkp:
        n_li.append(i)
print(n_li) """
        
    
            
        
                
                
        
        
         
