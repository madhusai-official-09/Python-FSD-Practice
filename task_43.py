# 1. A company's system records daily sales. Find the maximum number of consecutive days where the sales keep increasing. If the next day's sales are equal to or lower than the previous day, the streak starts again.
# Input:
# 100 120 150 140 160 180 200 190 210
# Output:
# 4
# Explanation:
# The longest increasing streak is:
# 140 → 160 → 180 → 200
# So, the answer is 4 

""" def max_sales(sales):
    current_count = 1
    max_count = 1
    for i in range(1,len(sales)):
        if sales[i] > sales[i-1]:
            current_count+=1
            max_count = max(current_count,max_count)
            
        else:
            current_count = 1
    return max_count

sales = [100, 120, 150, 140, 160, 180, 200, 190, 210]
ans = max_sales(sales)
print(ans) """

# 2. A company receives a large customer log string and needs to identify the smallest continuous portion that contains all required characters.
# Given two strings S and T, find the minimum-length substring of S that contains every character of T with the required frequency.
# If no such substring exists, print -1.
# Input:
# S = "ADOBECODEBANC"
# T = "ABC"
# Output:
# BANC
# Example 2:
# S = "AAABBC"
# T = "AABC"
# Output:
# AABBC



