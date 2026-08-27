
# 1. Write a Python function to return the *longest word* in a given sentence. If multiple words have the same maximum length, return the *first* one. 
# Input: Python is an amazing programming language 
# Output: programming 
# Explanation: Find the word with the m

""" def longestword(st):
    g=0
    m=''
    for i in st.split():
        if(g<len(i)):
            g=len(i)
            m=i
    return m
       
s = "Python is an amazing programming language"
ans = longestword(s)
print(ans) """

# 2. Write a Python function to return a new string by moving all *uppercase letters* to the beginning, followed by all *lowercase letters*, while preserving their original order. 
# Input: PyThOnProGram 
# Output: PTOPGyhnroram 
# Explanation: Collect all uppercase l

""" def move_uppercase(s):
    upper = ""
    lower = ""
    for i in s:
        if i.upper() == i:
            upper+=i
        else:
            lower+=i
    return upper+lower

st = "PyThOnProGram"
ans = move_uppercase(st)
print(ans) """

# 3. Write a Python function to return all characters that appear *exactly twice* in a string.
# Input:
# programming
# Output:
# r g m
# Explanation:
# Return all characters whose frequency is exactly 2.

""" def count_ch(st):
    n_st = ""
    for i in st:
        if st.count(i) == 2:
            n_st+=i
    return n_st
            
s = "programming"
ans = count_ch(s)
print(ans) """

# 4. Write a Python function to return the *first non-repeating character* in a string.
# Input:
# aabbccddefg
# Output:
# e
# Explanation:
# Return the first character whose frequency is 1.

""" def nonrepeatingch(st):
    for i in st:
        if st.count(i) == 1:
            return i
    
s = "aabbccddefg"
ans = nonrepeatingch(s)
print(ans) """

# 5. Write a Python function to check whether two strings are *rotations* of each other.
# Input:
# s1 = "rotation"
# s2 = "tionrota"
# Output:
# True*

""" def rotation_st(st1,st2):
    if st1 in st2+st2:
        return True
    else:
        return False
    
s1 = "rotation"
s2 = "tionrota"
ans = rotation_st(s1,s2)
print(ans) """
