
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

# 2. Write a Python function to return a new string by moving all *uppercase letters* to the beginning, followed by all *lowercase letters*, while preserving their original order. Input: PyThOnProGram Output: PTOPGyhnroram Explanation: Collect all uppercase l
