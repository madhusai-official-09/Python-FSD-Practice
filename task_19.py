# 1.Write a Python program to create a new tuple by inserting the index of every element immediately after it.
# Input:
# (10, 20, 30, 40)
# Output:
# (10, 0, 20, 1, 30, 2, 40, 3)
# Explanation:
# Create a new tuple by inserting the index of each element immediately after that element.

""" tu = (10, 20, 30, 40)
n_tu = []
for i in tu:
    idx = tu.index(i) 
    n_tu.append(i)
    n_tu.append(idx)
print(tuple(n_tu)) """

# 2.Write a Python program to create a new tuple by repeating every element according to its position.
# Input:
# (10, 20, 30, 40)
# Output:
# (10, 20, 20, 30, 30, 30, 40, 40, 40, 40)
# Explanation:
# Repeat the element at index 0 once, index 1 twice, index 2 three times, and so on.

""" tu =(10, 20, 30, 40)
n_tu = []
for i in tu:
    idx = tu.index(i)
    j = 0
    while j<=idx:
        n_tu.append(i)
        j+=1
print(tuple(n_tu)) """

# 3.Write a Python program to create a new tuple by inserting the sum of digits of every element immediately after that element.
# Input:
# (12, 35, 101)
# Output:
# (12, 3, 35, 8, 101, 2)
# Explanation:
# Insert the sum of digits of each element immediately after that element.

""" tu = (12, 35, 101)
n_tu = []
for i in tu:
    s = 0
    num = i
    while num>0:
        d = num%10
        num//=10
        s+=d
    n_tu.append(i)
    n_tu.append(s)
print(tuple(n_tu)) """
    
# 4.Write a Python program to create a new tuple containing only those elements that are greater than the average of the tuple.
# Input:
# (10, 25, 15, 30, 20)
# Output:
# (25, 30)
# Explanation:
# Average = 20. Create a new tuple containing only the elements greater than the average.

""" tu = (10, 25, 15, 30, 20)
avg = sum(tu)//len(tu)
n_tu = []
for i in tu:
    if i>avg:
        n_tu.append(i)
print(tuple(n_tu)) """

# 5.Write a Python program to create a new tuple by replacing every even-index element with its square and every odd-index element with its cube.
# Input:
# (2, 3, 4, 5, 6)
# Output:
# (4, 27, 16, 125, 36)
# Explanation:
# * Even index → Square the element.
# * Odd index → Cube the element.

""" tu = (2, 3, 4, 5, 6)
n_tu = []
for i in tu:
    idx = tu.index(i)
    if idx%2==0:
        n_tu.append(i**2)
    else:
        n_tu.append(i**3)
print(tuple(n_tu)) """
