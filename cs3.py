# 1. Write a Python program to insert the square of every odd number immediately after it in the same list.
# Input:
# Enter the list: [3, 4, 5, 8, 7]
# Output:
# [3, 9, 4, 5, 25, 8, 7, 49] 

""" li = [3,4,5,8,7]
n_li = []
for i in li:
    if i%2!=0:
        n_li.append(i)
        n_li.append(i**2)
    else:
        n_li.append(i)
print(n_li) """

# 2. Write a Python program to move all even numbers to the beginning of the list while maintaining their original order.
# Input:
# Enter the list: [7, 2, 9, 4, 5, 8, 1, 6]
# Output:
# [2, 4, 8, 6, 7, 9, 5, 1] 

""" li = [7, 2, 9, 4, 5, 8, 1, 6]
n_li = []
for i in li:
    if i%2==0:
        n_li.append(i)
for j in li:
    if j%2!=0:
        n_li.append(j)
print(n_li) """

# 3. Write a Python program to find the most frequently occurring element in a list.
# Input:
# Enter the list: [10, 20, 30, 20, 40, 20, 10, 20]
# Output:
# Most Repeated Element: 20
# Frequency: 4 

""" li = [10, 20, 30, 20, 40, 20, 10, 20]
max_element = 0
max_freq = 0
for i in li:
    freq = li.count(i)
    if freq>max_freq:
        max_freq = freq
        max_element = i
print(max_element)
print(max_freq) """

# 4. Write a Python program to find the first non-repeating element in a list.
# Input:
# Enter the list: [4, 2, 4, 5, 2, 7, 5, 8]
# Output:
# First Non-Repeating Element: 7 

""" li = [4, 2, 4, 5, 2, 7, 5, 8]
first = 0
for i in li:
    freq = li.count(i)
    if freq==1:
        first = i
        break
print(first) """
    
