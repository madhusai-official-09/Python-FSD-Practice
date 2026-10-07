# Case Study 
# 1. Write a Python program to find the first index where the sum of all elements on the left side is equal to the sum of all elements on the right side.Do not include the element at the current index in either sum. 
# Input:  
# Output:  
# Equilibrium Index: 2 

""" a = [1, 3, 5, 2, 2] 
def eq_index(lst):
    for i in range(len(lst)):
        right = lst[i+1:] 
        left = lst[0:i]
        if sum(right) == sum(left):
            return f"Equilibrium Index: {i}"  
print(eq_index(a)) """

# 2. Write a Python program to arrange the elements of a list according to their frequency in descending order. If two elements have the same frequency, maintain their original order.Do not use Counter() or sort(). 
# Input:  
# Output:  
# [4, 4, 4, 5, 5, 6, 6, 7] 

""" a = [4, 5, 6, 4, 5, 4, 7, 6] 
def freq_desc(lst):
    n_li = []
    p = []
    for i in lst:
        count = 0
        for j in lst:
            if i==j:
                count+=1
        if i not in p:
            p.append(i)
            if count>=1:
                n_li.extend([i]*count)
    return n_li
    
print(freq_desc(a)) """

# 3. Write a Python program to merge all overlapping intervals in a given list. Do not use any built-in interval or sorting functions. 
# Input:  
# Output:  
# Merged Intervals: [[1, 6], [8, 12]]
""" m = [[1, 3], 
    [2, 6], 
    [8, 10], 
    [9, 12]] 
n_li = []

for i in range(len(m)-1):
    temp = m[i]
    next_temp = m[i+1]
    if next_temp[0] > temp[0] and next_temp[0]<temp[1]:
        n_li.append(min(temp))
        n_li.append(max(next_temp))
        print(n_li)
    else:
        n_li.clear() """
    
