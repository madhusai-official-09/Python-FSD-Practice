# 1. Write a Python program to find all pairs of elements whose sum is equal to the given target.
# Input:
# (2, 7, 11, 15, 3, 8)
# Target = 10
# Output:
# [(2, 8), (7, 3)]

""" tu = (2, 7, 11, 15, 3, 8)
target = 10
pairs = []
for i in range(len(tu)):
    for j in range(i+1, len(tu)):
        if tu[i] + tu[j] == target:
            pairs.append((tu[i], tu[j]))
print(pairs) """

# 2. Write a Python program to remove all duplicate elements from a tuple while maintaining the original order.
# Input:
# (10, 20, 10, 30, 20, 40, 30, 50)
# Output:
# (10, 20, 30, 40, 50)

""" tu = (10, 20, 10, 30, 20, 40, 30, 50)
n_tu = []
for i in tu:
    if i not in n_tu:
        n_tu.append(i)
print(tuple(n_tu)) """

# 3. Write a Python program to find the longest continuous sequence of the same element in a tuple.
# Input:
# (1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5)
# Output:
# 4
# Explanation:
# The number 4 occurs continuously 4 times, which is the longest continuous sequence.

""" tu = (1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 4, 5)
cnt = 1
for i in tu:
    if tu.count(i) > cnt:
        cnt = tu.count(i)
print(cnt) """

# 4. Write a Python program to split a tuple into two tuples: one containing elements at even indices and another containing elements at odd indices.
# Input:
# (10, 20, 30, 40, 50, 60, 70, 80)
# Output:
# Even Index Tuple: (10, 30, 50, 70)
# Odd Index Tuple: (20, 40, 60, 80)

""" tu = (10, 20, 30, 40, 50, 60, 70, 80)
even = [] 
odd = []
for i in tu:
    if tu.index(i)%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even Index Tuple:", tuple(even))
print("Odd Index Tuple:", tuple(odd)) """

# 5. Write a Python program to check whether a tuple is a palindrome without converting it into a list.
# Input:
# (10, 20, 30, 20, 10)
# Output:
# Palindrome

""" tu = (10, 20, 30, 20, 10)
res = tu[::-1]
if tu == res:
    print("Palindrome") """

# 6. Write a Python program to find the common elements between two sets.
# Input:
# Set1 = {10, 20, 30, 40, 50}
# Set2 = {30, 40, 50, 60, 70}
# Output:
# {30, 40, 50}

""" Set1 = {10, 20, 30, 40, 50}
Set2 = {30, 40, 50, 60, 70}
common = Set1.intersection(Set2)
print(common) """

# 7. Write a Python program to find all elements that are present in the first set but not in the second set.
# Input:
# Set1 = {10, 20, 30, 40, 50}
# Set2 = {30, 40, 60, 70}
# Output:
# {10, 20, 50}

""" Set1 = {10, 20, 30, 40, 50}
Set2 = {30, 40, 60, 70}
diff = Set1.difference(Set2)
print(diff) """