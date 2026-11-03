# 1.Write a Python program to check whether two strings are isomorphic. Two strings are isomorphic if each character in the first string can be mapped to exactly one character in the second string, while maintaining the character order. 
# Input: str1 = "paper" , t = "title"
# output: True
# explanation: 'p' -> 't', 'a' -> 'i', 'p' -> 't', 'e' -> 'l', 'r' -> 'e'

str1 = "paper"
t = "title"

dic = {}
if len(str1) == len(t):
    for i in range(len(str1)):
        if str1[i] in dic:
            dic[str1[i]].append(i)
        else:
            dic[str1[i]]




