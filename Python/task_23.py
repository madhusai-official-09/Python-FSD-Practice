# 1.Write a Python program to group all keys having the same value into a list.
# Input:
# d = {"a": 10,"b": 20,"c": 10,"d": 30,"e": 20,"f": 10}
# Output:
# {10: ['a', 'c', 'f'],20: ['b', 'e'],30: ['d']}

""" d = {"a": 10,"b": 20,"c": 10,"d": 30,"e": 20,"f": 10}
n_d = {}
for i in d:
    if d[i] not in n_d:
        n_d[d[i]] =[i]
    else:
        n_d[d[i]].append(i)
print(n_d) """

# 2.Write a Python program to arrange the dictionary in ascending order of values without using the built-in sorted() function.
# Input:
# d = {"A": 45,"B": 12,"C": 78,"D": 30,"E": 56}
# Output:
# {"B": 12,"D": 30,"A": 45,"E": 56,"C": 78}

""" d = {"A": 45,"B": 12,"C": 78,"D": 30,"E": 56}
d1 = list(d.items())
for i in range(0,len(d1)-1):
    for j in range(0,len(d1)-i-1):
        if d1[j][1]>d1[j+1][1]:
            d1[j+1],d1[j]=d1[j],d1[j+1]
ans = {k:v for k,v in d1}
print(ans) """

# 3.Write a Python program to find all keys whose values are prime numbers.
# Input:
# d = {"a": 12,"b": 17,"c": 23,"d": 25,"e": 31}
# Output:
# ['b', 'c', 'e']

""" d = {"a": 12,"b": 17,"c": 23,"d": 25,"e": 31}
ans = []
for k,v in d.items():
    num = v
    i=1
    count = 0
    while i<=num:
        if num%i==0:
            count+=1
        i+=1
    if count==2:
        ans.append(k)
print(ans) """

# 4.Write a Python program to find the row whose sum is maximum in a nested list. If two rows have the same sum, consider the first one.
# Input:
# x = [ [10, 20, 5],[15, 8, 12],[25, 5, 10],[7, 18, 20] ]
# Output:
# [7, 18, 20]
# Sum: 45

""" x = [ [10, 20, 5],[15, 8, 12],[25, 5, 10],[7, 18, 20] ]
s = 0
for i in x:
    temp = i
    s1 = sum(temp)
    if s1>s:
        s = s1
        a = temp
print(a)
print("Sum:",s) """

# 5.Write a Python program to remove duplicate tuples from a nested tuple while maintaining the original order.
# Input:
# x = ((1, 2),(3, 4),(1, 2),(5, 6),(3, 4),(7, 8))
# Output:
# ((1, 2), (3, 4), (5, 6), (7, 8))

""" x = ((1, 2),(3, 4),(1, 2),(5, 6),(3, 4),(7, 8))
ans = []
for i in x:
    for j in x:
        if i==j:
            if i not in ans:
                ans.append(i)
                
print(tuple(ans)) """
    
    
    


    
    