# 1.Write a Python function to count the number of words that contain at least two vowels.
# Input:
# Python is easy to learn
# Output:
# 2
# Explanation:
# Count the words that contain at least two vowels.

""" def count_words(st):
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
    return word_count
st = "Python is easy to learn"
result = count_words(st)
print(result) """

# 2.Write a Python function to find the first character that appears more than once in a string.
# Input:
# abcaefbd
# Output:
# a
# Explanation:
# The character a is the first character that appears more than once.

""" def first_ch(st):
    output = {}
    for i in st:
        if i not in output:
            output[i] = 1
        else:
            output[i] += 1
    for i in output:
        if output[i] > 1:
            return i
            
st = "abcaefbd"
result = first_ch(st)
print(result)  """ 
  
# 3.Write a Python function to check whether a string contains all unique characters.
# Input:
# python
# Output:
# True
# Explanation:
# Return True if no character appears more than once; otherwise, return False.

""" def un_ch(st):
    new_st = {}
    for i in st:
        if i not in new_st:
            new_st[i] = 1
        else:
            new_st[i] += 1
    for i in new_st:
        if new_st[i] > 1:
            return False
    return True
st = "Python"
res = un_ch(st)
print(res) """

# 4.Write a Python function to create a new dictionary by assigning a rank to each key based on its value in descending order. The highest value should get rank 1.
# Input:
# {'A': 85, 'B': 92, 'C': 78, 'D': 88}
# Output:
# {'B': 1, 'D': 2, 'A': 3, 'C': 4}
# Explanation:
# Assign ranks based on the values in descending order. The key with the highest value gets rank 1, the next highest gets rank 2, and so on.

""" def rank_descending_order(dic):
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
        for j in range(i+1,len(li)):
            if li[i][1] > li[j][1]:
                li[i],li[j] = li[j],li[i]
    res ={k:v for k,v in li}
    return res
dic = {'A': 85, 'B': 92, 'C': 78, 'D': 88}
result = rank_descending_order(dic)
print(result) """

# 5. Write a Python function to check whether two lists are rotations of each other. Input: [1, 2, 3, 4, 5] [3, 4, 5, 1, 2] 
# Output: True 
# Explanation: Return True if one list can be obtained by rotating the other; otherwise, return False.

""" def check_rotation(li1, li2):
    if len(li1) != len(li2):
        return False
    for i in range(len(li1)):
        li1.append(li1[0])
        li1.pop(0)
        if li1 == li2:
            return True
    return False    
li1 = [1, 2, 3, 4, 5]
li2 = [3, 4, 5, 1, 2]
result = check_rotation(li1, li2)
print(result) """