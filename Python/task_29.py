# 1. Write a Python program to create a new string by placing all digits at the beginning, followed by all alphabets, while preserving their original order. 
# Input: ab12cd34ef5 
# Output: 12345abcdef

""" def dig_begin(st):
    word = ""
    num = ""
    for i in st:
        if i.isnumeric() == True:
            num+=i
        else:
            word+=i
    return num+word
  
s = "ab12cd34ef5"
ans = dig_begin(s)
print(ans) """

# 2. Write a Python program to print all characters whose ASCII value is a prime number. 
# Input: ABCDEF 
# Output: C

""" def isprime(num):
    for d in range(2,(num//2)+1):
        if num%d == 0:
            return False
    else:
        return True
    
def ascii_prime(st):
    for i in st:
        ascii = ord(i)
        prime = isprime(ascii)
        if prime == True:
            return i
        
s = "ABCDEF"
ans = ascii_prime(s)
print(ans)  """

# 3. Write a Python program to find the longest substring without repeating characters. 
# Input: abcabcbb 
# Output: abc

""" s = "abcabcbb"
b = 0
f = ""
for i in range(0,len(s)):
    for j in range(i+1,len(s)):
        res = s[i:j]
        if len(res) == len(set(res)):
            if b<len(res):
                b = len(res)
                f = res
print(f) """

# 4. Write a Python program to reverse each word in a given sentence while keeping the order of the words unchanged. 
# Input: Python is easy 
# Output: nohtyP si ysae

""" s = "Python is easy"
def rev_word(st):
    word = ""
    for i in st.split():
        word+=i[::-1]
        word+=" "
    return word

ans = rev_word(s)
print(ans) """

# 5. Write a Python program to find the smallest word in a given sentence. If multiple words have the same minimum length, print the first one. 
# Input: Python is an amazing programming language 
# Output: is

""" s = "Python is an amazing programming language"
f = 0
g = ""
for i in s.split():
    min = len(i)
    if f == 0 or f > min:
        f = min
        g = i
print(g) """

