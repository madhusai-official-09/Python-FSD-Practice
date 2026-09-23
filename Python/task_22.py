# 1.Write a Python program to count the frequency of each element in a list using a dictionary.
# Input:
# [1, 2, 3, 2, 1, 2, 4]
# Output:
# {1: 2, 2: 3, 3: 1, 4: 1}

""" li = [1, 2, 3, 2, 1, 2, 4]
n_li = {}
for i in li:
    if i in n_li:
        n_li[i] += 1
    else:
        n_li[i] = 1
print(n_li) """

# 2.Write a Python program to find the key having the highest value in a dictionary.
# Input:
# {"a": 10, "b": 25, "c": 15, "d": 30}
# Output:
# d

""" di = {"a": 10, "b": 25, "c": 15, "d": 30}
n_du = 0
for i in di:
    if di[i] > n_du:
        n_du = di[i]
        key = i
print(key) """

# 3.Write a Python program to calculate the sum of all values in a dictionary without using sum().
# Input:
# {"a": 10, "b": 20, "c": 30}
# Output:
# 60

""" di = {"a": 10, "b": 20, "c": 30}
n_di = 0
for i in di:
    n_di+=di[i]
print(n_di) """

# 4.Write a Python program to count the occurrence of each character in a string using a dictionary.
# Input:
# programming
# Output:
# {"p": 1, "r": 2, "o": 1, "g": 2, "a": 1, "m": 2, "i": 1, "n": 1}

""" di = "programming"
n_di = {}
for i in di:
    if i in n_di:
        n_di[i] += 1
    else:
        n_di[i] = 1
print(n_di) """

# 5.Write a Python program to find the key and value whose value is the second highest in a dictionary.
# Input:
# {"A": 80, "B": 95, "C": 70, "D": 90}
# Output:
# D-90

""" di = {"A": 80, "B": 95, "C": 70, "D": 90}
first = 0
second = 0
for i in di:
    if di[i] > first:
        second = first
        first = di[i]
        key=i
    elif di[i] > second:
        second = di[i]
        key = i
print(f"{key}-{second}") """        
