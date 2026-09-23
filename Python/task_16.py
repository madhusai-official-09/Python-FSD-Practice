# 1. Write a Python program to insert the reverse of every two-digit number immediately after it in the same list.

# Input:
# [12, 8, 45, 123, 67]

# Output:
# [12, 21, 8, 45, 54, 123, 67, 76]

""" li = [12, 8, 45, 123, 67]
n_li = []
for i in li:
    n_li.append(i)
    if i>=10 and i<=99:
        rev = int(str(i)[::-1])
        n_li.append(rev)
print(n_li) """

# 2. Write a Python program to move all the zeros to the end of the list while maintaining the relative order of the non-zero elements.

# Input:
# [0, 5, 0, 8, 3, 0, 2, 1]

# Output:
# [5, 8, 3, 2, 1, 0, 0, 0]

""" li = [0, 5, 0, 8, 3, 0, 2, 1]
for i in li:
    if i==0:
        li.remove(i)
        li.append(i)
print(li) """

# 3. Write a Python program using slicing to swap the first and last three elements of the given list.

# Input:
# [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Output:
# [70, 80, 90, 40, 50, 60, 10, 20, 30]

""" li = [10, 20, 30, 40, 50, 60, 70, 80, 90]
mid = len(li)//2
li[:3] , li[-3:] = li[-3:], li[:3]
print(li) """
    
# 4. Write a Python program using slicing to divide the given list into four equal parts and print each part separately.

# Input:
# [10, 20, 30, 40, 50, 60, 70, 80]

# Output:

# [10, 20]
# [30, 40]
# [50, 60]
# [70, 80]

""" li = [10, 20, 30, 40, 50, 60, 70, 80]
n = len(li)//4
for i in range(0, len(li), n):
    print(li[i:i+n]) """
    
# 5. Write a Python program using slicing to reverse only the middle four elements of the given list.

# Input:
# [10, 20, 30, 40, 50, 60, 70, 80]

# Output:
# [10, 20, 60, 50, 40, 30, 70, 80]

""" li = [10, 20, 30, 40, 50, 60, 70, 80]
li[2:6] = li[2:6][::-1]
print(li) """

# 6. Write a Python program using List Comprehension to create a new list containing the square of each number that is divisible by 3 but not divisible by 2.

# Input:
# [3, 6, 9, 12, 15, 18, 21, 24]

# Output:
# [9, 81, 225, 441]

""" li = [3, 6, 9, 12, 15, 18, 21, 24]
n_li = [i**2 for i in li if i%3==0 and i%2!=0]
print(n_li) """

# 7. Write a Python program using List Comprehension to replace every negative number with 0 while keeping all other elements unchanged.

# Input:
# [-5, 12, -8, 20, 0, -3, 15]

# Output:
# [0, 12, 0, 20, 0, 0, 15]

""" li = [-5, 12, -8, 20, 0, -3, 15]
n_li = [i if i>=0 else 0 for i in li]
print(n_li) """