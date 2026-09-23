# 1. Write a Python program to find the difference between the largest and smallest elements in a given list.
# Input:
# [18, 7, 25, 12, 30]
# Output:
# 23

""" li = [18, 7, 25, 12, 30]
largest = li[0]
smallest = li[0]
for i in li:
    if i > largest:
        largest = i
    if i < smallest:
        smallest = i
value = largest - smallest
print(value) """

# 2. Write a Python program to create a new list containing only the numbers whose sum of factors is a Perfect Square.
# Input:
# [1, 3, 22, 66, 70, 81, 94]
# Output:
# [1, 3, 22, 66, 70, 81, 94]

""" li = [1, 3, 22, 66, 70, 81, 94]
n_li = []
for i in li:
    num = 1
    s = 0
    while num<=i:
        if i%num==0:
            s += num
        num+=1
    sqr = s**(0.5)
    if sqr*sqr == s:
        n_li.append(i)
print(n_li) """ 

# 3. Write a Python program to create a new list containing only the numbers for which the difference between the number and its reverse is divisible by 9.
# Input:
# [12, 15, 23, 41, 56]
# Output:
# [12, 15, 23, 41, 56]

""" li = [12, 15, 23, 41, 56]
n_li = []
for i in li:
    num = i
    rev = 0
    while num >0:
        d = num%10
        rev = rev*10+d
        num//=10
    result = abs(rev-i)
    if result%9==0:
        n_li.append(i)
print(n_li) """

                       # List Slicing Problems
                       
# 4. Write a Python program to print the list excluding the first and last elements using slicing.
# Input:
# [10, 20, 30, 40, 50, 60, 70]
# Output:
# [20, 30, 40, 50, 60]

""" li = [10, 20, 30, 40, 50, 60, 70]
n_li = li[1:len(li)-1]
print(n_li) """

# 5. Write a Python program to print the list in reverse order using slicing.
# Input:
# [10, 20, 30, 40, 50, 60]
# Output:
# [60, 50, 40, 30, 20, 10]

""" li = [10, 20, 30, 40, 50, 60]
n_li = li[::-1]
print(n_li) """

# 6. Write a Python program to print every second element of the given list using slicing.
# Input:
# [10, 20, 30, 40, 50, 60, 70, 80]
# Output:
# [10, 30, 50, 70]

""" li = [10, 20, 30, 40, 50, 60, 70, 80]
n_li = li[::2]
print(n_li) """

# 7. Write a Python program to print the list from the 3rd element to the 6th element using slicing.
# Input:
# [10, 20, 30, 40, 50, 60, 70, 80]
# Output:
# [30, 40, 50, 60]

""" li = [10, 20, 30, 40, 50, 60, 70, 80]
n_li = li[2:6]
print(n_li) """

