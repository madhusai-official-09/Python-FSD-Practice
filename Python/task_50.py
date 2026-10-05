# Write a function analyze_list() that accepts a list of integers and returns three values:
# 1. The largest element that occurs only once
# 2. The smallest element that occurs more than once
# 3. The total number of elements that are repeated
# Do not use max(), min(), or count().
# Input:
# a = [7, 3, 9, 3, 5, 7, 2, 9, 9, 4, 6, 6]


# Output:
# Largest unique = 5
# Smallest repeated = 3
# Repeated elements count = 4

    
def analyze_list(lst):
    largest = 0
    small = 9
    unq = []
    unq_count = 0
    for i in lst:
        count = 0
        for j in lst:
            if i == j:
                count+=1
                  
        if count == 1:
            if i > largest:
                largest = i
                
        elif count > 1:
            if i < small:
                small = i
                
        if count>1:
            if i not in unq:
                unq.append(i)
                unq_count+=1
    return f"Largest unique = {largest}\nSmallest repeated = {small}\nRepeated elements count = {unq_count}"
                

a = [7, 3, 9, 3, 5, 7, 2, 9, 9, 4, 6, 6]
print(analyze_list(a))