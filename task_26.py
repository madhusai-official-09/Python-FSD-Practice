# 1.Write a Python function to count the number of words that contain at least two vowels.
# Input:
# Python is easy to learn
# Output:
# 2
# Explanation:
# Count the words that contain at least two vowels.

""" st = "Python is easy to learn"
vowels = "aeiouAEIOU"
li = st.split()
word_count = 0
for word in li:
    temp = str(word.lower())
    count = 0
    for i in temp:
        for j in vowels:
            if i == j:
                count+=1   
    if count>=2:
        word_count+=1
print(word_count) """

# 2.Write a Python function to find the first character that appears more than once in a string.
# Input:
# abcaefbd
# Output:
# a
# Explanation:
# The character a is the first character that appears more than once.

""" st = "abcaefbd"
count = 0
for i in st:
    if st[0] == i:
        count +=1
if count>1:
    print(st[0]) """
    
# 3.Write a Python function to check whether a string contains all unique characters.
# Input:
# python
# Output:
# True
# Explanation:
# Return True if no character appears more than once; otherwise, return False.

""" st = "Python"
def un_ch(str):
    for i in str:
        if i not in str:
            print(i)
res = un_ch(st)
print(res) """

# 4.Write a Python function to create a new dictionary by assigning a rank to each key based on its value in descending order. The highest value should get rank 1.
# Input:
# {'A': 85, 'B': 92, 'C': 78, 'D': 88}
# Output:
# {'B': 1, 'D': 2, 'A': 3, 'C': 4}
# Explanation:
# Assign ranks based on the values in descending order. The key with the highest value gets rank 1, the next highest gets rank 2, and so on.

dic = {'A': 85, 'B': 92, 'C': 78, 'D': 88}
output= {}
for i in dic:
    if dic[i] > 90:
        output[i]=1
    elif dic[i]>85:
        output[i] =2
    elif dic[i]>80:
        output[i]=3
    else:
        output[i]=4
li = list(output.items())
for i in range(0,len(li)-1):
    if li[i][1] >= li[i+1][1]:
        li[i],li[i+1] = li[i+1],li[i]
res ={k:v for k,v in li}
print(res)

    