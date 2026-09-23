# 1. Write a recursive function flatten(lst) that converts a nested list into a single flat list. 
# Input: lst = [1, [2, 3], [4, [5, 6]], 7] 
# Output: [1, 2, 3, 4, 5, 6, 7]

""" def flatten(lst,output = []):
    for i in lst:
        if type(i)==list:
            flatten(i)
        else:
            output.append(i)
    return output
print(flatten([1, [2, 3], [4, [5, 6]], 7])) """

# 2. Write a recursive function nested_sum(lst) that calculates the sum of all numbers present inside a nested list, regardless of the nesting level. 
# Input: lst = [1, [2, [3, 4]], [5, [6, [7]]]] 
# Output: 28

""" def nested_sum(lst,output = [],s = 0):
    for i in lst:
        if type(i)==list:
            nested_sum(i)
        else:
            output.append(i)
    for k in output:
        s +=k
    return s

print(nested_sum([1, [2, [3, 4]], [5, [6, [7]]]])) """

# 3. Create two decorators: ascending → sorts the list returned by the function in ascending order. descending → sorts the list returned by the function in descending order. Apply the appropriate decorator to the function and display both results. Input: def g

""" def dec_ascending(fun):
    def inner(li):
        return sorted(li)
    return inner

def dec_descending(fun):
    def inner(li):
        ans = sorted(li)
        return ans[::-1]
    return inner

@dec_descending
def list_order(li,n_li=[]):
    for i in li:
        n_li.append(i)
    return n_li

li = [4,2,6,1,5,3]
print(list_order(li)) """

# 4. Write a Python generator function that takes a number n and divides it into 4 equal parts. If n is not exactly divisible by 4, add the remaining value only to the last part. 
# Input: n = 103 
# Output: 25 25 25 28

""" def four_part(n):
    i = 1
    d = 4
    while i<=d:
        if n%d==0:
            res = n//d
            yield res
        else:
            if n%d!=0 and i<=3:
                q = n//d
                yield q
            elif i==4:
                q=n//d
                r = n-4*q
                res=q+r
                yield res 
        i+=1
n = 105
for i in four_part(n):
    print(i) """
    
def fourparts(n):
    p=n//4
    while n>p:
        if n>2*p:
            yield p
        else:
            yield n
        n=n-p
n=103
for i in fourparts(n):
    print(i)