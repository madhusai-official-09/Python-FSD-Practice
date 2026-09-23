# 1. Write a Python Program using two decorators:
# ->The first decorator should convert all vowels in the returned string to uppercase.
# ->The second decorator shoould add *** at tthe beginning and end of the returned string.
# Input: s = "hello world"
# output: ***hEllO wOrld***

# def vowel_uppercase(fun):
#     def inner(s):
#         st = fun(s)
#         vowels = "aeiouAEIOU"
#         for i in st:
#             if i in vowels:
#                 st = st.replace(i, i.upper())
#         return st
        
#     return inner 

# def add_stars(fun):
#     def inner(s):
#         st = fun(s)
#         return "***" + st + "***"
#     return inner

# @vowel_uppercase
# @add_stars
# def process_string(s):
#     return s

# print(process_string("hello world"))

# 2. Write a python program using a generator to yield each word from a string in reverse order, but keep the characters of each word unchanged.
# Input : s = "Python is very powerful"
# Output:
# powerful
# very
# is 
# Python 

""" def reverse_word(s):
    word = s.split()
    for i in range(len(word)):
        yield word[len(word) - 1 - i]
        
ans = reverse_word("Python is very powerful")
for ch in ans:
    print(ch) """
    
# 3. Write a recursive function that repeatedly calculates the sum of digits of a number until a single-digit number is obtained.
# Input: n=98756
# output: 8

""" def sum_of_digits(n):
    if n<10:
        return n
    else:
        last_digit = n%10
        return sum_of_digits(n//10+last_digit)
    
print(sum_of_digits(98756)) """