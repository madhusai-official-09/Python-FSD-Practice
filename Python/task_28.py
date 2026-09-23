# 1.Write a Python program to compress a string.
# Input : aaabbc
# Output : a3b2c1


""" def count_ch(st):
    word = ""
    for i in st:
        count = 0
        for j in st:
            if i==j:
                count+=1
        if i not in word:
            word+= i+str(count)
    return word

s = "aaabbc"
ans = count_ch(s)
print(ans) """

# 2. Write a Python program to create a mirror string.
# Input : abc
# Output : abccba

""" s = "abc"
def mirror_string(st):
    word = ""
    for i in st:
        word+=i
    for j in st[::-1]:
        word+=j
    return word

ans = mirror_string(s)
print(ans) """

# 3. Write a Python program to find the longest palindromic substring.
# Input : babad
# Output : bab

""" def ispalindrome(st):
    b=0
    f=''
    for i in range(0,len(st)):
        for j in range(i+1,len(st)):
            res=st[i:j]
            if(res==res[::-1]):
                if(b<len(res)):
                    b=len(res)
                    f=res
    return f
    
s = "babad"
ans = ispalindrome(s)
print(ans) """

# 4.Write a Python function to remove all special characters from a string.
# Input : a@1#b
# Output : a1b

""" st = "a@1#b"
def spl_ch(s):
    word = ""
    for i in s:
        if i.isalpha() == True or i.isnumeric():
            word+=i
    return word

ans = spl_ch(st)
print(ans) """

# 5.Write a Python function to reverse every alternate word in a sentence.
# Input : one two three four
# Output : one owt three ruof

""" st = "one two three four"
def rev_alt_word(s):
    temp = s.split()
    word = ""
    for i in range(len(temp)):
        if i%2==0:
            word += temp[i]
            word+=" "
        else:    
            word += temp[i][::-1]
            word+=" "
    return word

ans = rev_alt_word(st)
print(ans) """

