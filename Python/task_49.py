# 1.Write a Python program to count the total number of vowels in a string. If the vowel count is odd, print False. If it is even, divide the string into two non-empty parts at the position where the number of vowels in the first part becomes exactly half of the total vowel count.
# input: "Hello World" Output: 3 False

""" def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    if count % 2 != 0:
        print(count, False)
    else:
        half_count = count//2
        current_count = 0
        for i, ch in enumerate(s):
            if ch in vowels:
                current_count += 1
            if current_count == half_count:
                print(count, s[:i+1], s[i+1:])
                break
count_vowels("Hello World") """


# 2.Write a Python program to find the index of the first element in a list whose value is equal to the sum of all elements before it. If no such element exists, print -1. Input: [4, 7, 11, 20, 30] Output: 2

def find_index(lst):
    for i in range(1, len(lst)):
        if lst[i] == sum(lst[:i]):
            return i
    return -1

print(find_index([4, 7, 11, 20, 30]))