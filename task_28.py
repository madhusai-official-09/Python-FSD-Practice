# 1.Write a Python program to compress a string.
# Input : aaabbc
# Output : a3b2c1

""" s = "aaabbc"

def count_ch(st):
    n_di = {}
    n_st = ""
    for i in st:
        if i in n_di:
            n_di[i] += 1
        else:
            n_di[i] = 1
    key = 
    return key

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

