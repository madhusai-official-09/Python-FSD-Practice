# 1. Write a Python function to rearrange a string so that each word is placed immediately after its reversed form. Preserve the original word order. 
# Input: hello world python 
# Output: hello olleh world dlrow python nohtyp

""" def rearrange(st):
    n_st = ""
    for i in st.split():
        n_st+=i
        n_st+=" "
        n_st+=i[::-1]
        n_st+=" "
    return n_st
s = "hello world python"
ans = rearrange(s)
print(ans) """

# 2. Write a Python function to find the longest word in a sentence that contains all unique characters. 
# Input: apple dream house coding 
# Output: dream

""" def longestword(st):
    for i in st.split():
        if len(i) == len(set(i)):
            return i
        
s = "apple dream house coding"
ans = longestword(s)
print(ans) """

# 3. Write a Python function to find the word whose characters have the highest total ASCII value. If multiple words have the same value, return the first one.
# Input: cat dog apple 
# Output: apple

""" def highasciival(st):
    highest = 0
    for i in st.split():
        total = 0
        for j in i:
            asci = ord(j)
            total += asci
        if  total>highest:
            highest = total
            word = i
    return word
  
s = "cat dog apple"
ans = highasciival(s)
print(ans)  """   

# 4. Write a Python function to decode a string where each alphabetic character is followed by a number indicating how many times it should be repeated. 
# Input: a3b2c4 
# Output: aaabbcccc

""" def decodestr(st):
    word = ""
    for i in range(len(st)):
        if st[i]>=chr(65) and st[i]<=chr(122):
            first = st[i]
        elif int(st[i])>=1 and int(st[i])<=9:
            second = int(st[i])
            word+=first*second
    return word
    
s = "a3b2c4"
ans = decodestr(s)
print(ans) """