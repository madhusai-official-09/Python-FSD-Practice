# 1. Write a Python function to find the maximum sum of any two consecutive elements in a list and return the elements that produce the maximum sum. 
# Input: [4, 7, 2, 9, 5, 12, 3] 
# Output: [5, 12]

""" def max_cons(li):
    s = 0
    n_li = []
    for i in range(len(li)-1):
        if li[i]+li[i+1]>s:
            s = li[i]+li[i+1]
            n_li.clear()
            n_li.append(li[i])
            n_li.append(li[i+1])
    return n_li

x = [4, 7, 2, 9, 5, 12, 3]
ans = max_cons(x)
print(ans) """

# 2. Write a Python function to remove consecutive duplicate characters from a string while keeping the first occurrence of each consecutive group. 
# Input: "aaabbccdaaee" 
# Output: "abcdae"

""" def remove_consecutive(s):
    a = ""
    for i in range(len(s)-1):
        if s[i]!=s[i+1]:
            a+=s[i]
    else:
        a+=s[i]
    return a
st = "aaabbccdaaee"
ans = remove_consecutive(st)
print(ans) """

# 3. Given a tuple of numbers, find the smallest positive number that is missing from the tuple. 
# Input: (3, 4, -1, 1, 2, 6) 
# Output: 5

""" def missing_number(tu):
    n_tu = sorted(tu)
    l_tu = 0
    for i in range(len(n_tu)-1):
        if n_tu[i]>0 and n_tu[i+1]!=n_tu[i]+1:
            l_tu = n_tu[i]+1
    return l_tu
            
tu = (3, 4, -1, 1, 2, 6)
ans = missing_number(tu)
print(ans) """
    
# 4. Write a Python program using a nested function and nonlocal to create a counter. The counter should start with the given value and increase by the corresponding values in the list. 
# Input: start = 5 
# values = [3, 7, 2, 8] 
# Output: 8 15 17 25

""" def outer():
    start = 5
    def inner():
        nonlocal start
        li = [3,7,2,8]
        for i in range (len(li)):
            if i==0:
                res = li[i]+start
                print(res)
            else:
                res+=li[i]
                print(res)
    return inner()
outer() """