# 1. Write a Python program to find the smallest substring of a given string that contains every character of a target string, including duplicate character requirements. If multiple windows have the same minimum length, return the earliest one.
# Input:
# s = "ADOBECODEBANCAB"
# target = "ABC"
# Output: BANC

""" s = "ADOBECODEBANCAB"
target = "ABC"

best_len = float("inf")
best_substring = ""
for i in range(len(s)):
    for j in range(i+1,len(s)):
        substring = s[i:j]
        
        c = 0
        for ch in target:
            if ch in substring:
                c+=1
        
        if c == len(target):
            if len(substring) < best_len:
                best_len = len(substring)
                best_substring = substring
print(best_substring) """

# 2. Write a Python program to evaluate a mathematical expression containing integers, parentheses, addition, subtraction, multiplication, division, and spaces. Follow standard operator precedence and support unary negative numbers.
# Input:
# expression = "-(12 + 8) * 3 + 40 / 5"
# Output:-52.0

expression = "-(12 + 8) * 3 + 40 / 5"
