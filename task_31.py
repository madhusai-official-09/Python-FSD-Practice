# 1. Write a Python function to find the longest palindrome substring in a given string. If multiple palindromes have the same length, return the one that appears first. 
# Input: "forgeeksskeegfor" 
# Output: "geeksskeeg"

""" def longest_palindrome(st):
    b = 0
    f = ""
    for i in range(0,len(st)):
        for j in range(i+1,len(st)):
            res = st[i:j]
            if res == res[::-1]:
                if b < len(res):
                    b = len(res)
                    f=res
    return f
    
s = "forgeeksskeegfor"
ans = longest_palindrome(s)
print(ans) """

# 2. Write a Python program to find the second-largest unique element from each tuple and store the results in a list. 
# Input: [(10, 5, 8, 10), (7, 12, 3, 9), (20, 15, 20, 18)] 
# Output: [8, 9, 18]

""" li = [(10, 5, 8, 10), (7, 12, 3, 9), (20, 15, 20, 18)]
n_li = []
for i in li:
    li = list(i)
    large = 0
    second = 0
    for j in li:
        if j > large:
            second = large
            large = j
        elif j>second  and j!=large:
            second = j
    n_li.append(second)
print(n_li) """

# 3. Set + List Write a Python program to find all elements that occur in the list more than once, but return them as a set without using count(). 
# Input: [4, 7, 2, 4, 9, 7, 3, 2, 8, 7] 
# Output: {2, 4, 7}

""" li = [4, 7, 2, 4, 9, 7, 3, 2, 8, 7]
n_li = []
for i in li:
    count = 0
    for j in li:
        if i == j:
            count+=1
    if count>1:
        n_li.append(i)
print(set(n_li)) """

# 4. Write a Python program using a nested function where the inner function modifies a variable from the outer function using nonlocal. Each call should increase the value by the given input. 
# Input: start = 10 
# values = [5, 8, 12] 
# Output: 15 23 35

""" def outer():
    x = 10
    def inner():
        nonlocal x
        li = [5,8,12]
        next = 0
        for i in range(len(li)):
            if i == 0:
                result = li[i]+x
                print(result)
            else:
                result += li[i]
                print(result)
    return inner()
outer() """