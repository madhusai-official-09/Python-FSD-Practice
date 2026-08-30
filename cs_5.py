# 1. Longest consecutive increasing subsequence 
""" li = [1,2,3,1,2,3,4,5,1,2,3,4,5]
n_li = []
for i in range(len(li)):
    if li[i] not in n_li:
        n_li.append(li[i])
print(n_li) """

# 2. decode a string.
""" st = "3[a]2[bc]"
n = ""
n_li = ""
for i in st: """

# 4. palindrome of string.
st = "aaa"
for i in range(len(st)):
    for j in range(i+1,len(st)):
        res = st[i:j]
        print(res,res[::-1])
    