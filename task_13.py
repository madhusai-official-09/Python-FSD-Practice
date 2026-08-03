# 1. Write a Python program to create a new list containing only the elements that are greater than the average of the given list.
# Input:
# [10, 20, 30, 40, 50]
# Output:
# [40, 50]

""" li = [10, 20, 30, 40, 50]
n_li =[]
n = len(li)
s = 0
for i in li:
    s+=i
avg = s//n
for i in li:
    if i>avg:
        n_li.append(i)
print(n_li) """

# 2. Write a Python program to create a new list containing only the numbers whose reverse is divisible by the original number.
# Input:
# [12, 22, 25, 44, 13]
# Output:
# [22, 44]

""" li = [12, 22, 25, 44, 13]
n_li = []
for i in li:
    num = i
    rev = 0
    while num>0:
        d = num%10
        rev = rev*10+d
        num//=10
    if rev%i==0:
        n_li.append(i)
print(n_li) """

# 3. Write a Python program to create a new list containing only the numbers whose sum of digits is greater than the product of their digits.
# Input:
# [12, 22, 111, 24, 123]
# Output:
# [111]

""" li = [12, 22, 111, 24, 123]
n_li = []
for i in li:
    num = i
    s = 0
    p=1
    while num>0:
        d = num%10
        s+=d
        p*=d
        num//=10
    if s>p:
        n_li.append(i)
print(n_li) """

# 4. Write a Python program to create a new list containing only the elements that are divisible by the sum of their digits.
# Input:
# [12, 18, 20, 25, 27, 30]
# Output:
# [12, 18, 20, 27, 30]

""" li = [12, 18, 20, 25, 27, 30]
n_li = []
for i in li:
    num = i
    s = 0
    while num>0:
        d = num%10
        s+=d
        num//=10
    if i%s==0:
        n_li.append(i)
print(n_li) """

# 5. Write a Python program to create a new list containing only the numbers whose first digit is equal to the last digit.
# Input:
# [11, 23, 44, 57, 99, 101]
# Output:
# [11, 44, 99, 101]

""" li = [11, 23, 44, 57, 99, 101]
n_li = []
for i in li:
    num = i
    first = 0
    last = num%10
    while num>0:
        d = num%10
        first = d
        num//=10
    if first==last:
        n_li.append(i)
print(n_li) """