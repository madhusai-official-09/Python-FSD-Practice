# 1. Write a function check_number(n) to print all the even numbers from 1 to n without using the % operator. 
# Input: n = 48 
# Output: 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48

""" def check_number(n):
    if n == 0:
        return
    else:
        (check_number(n-2))
        print(n)
    
check_number(48) """

# 2. Given three sets, write a function find_common(s1, s2, s3) to display all elements that are present in at least two of the three sets. 
# Input: s1 = {10, 20, 30, 40, 50} s2 = {20, 30, 60, 70} s3 = {30, 40, 80, 90} Output: 20 30 40

""" def find_common(s1,s2,s3):
    res1 = s1&s2
    res2 = s2&s3
    res3 = s3&s1
    ans = res1|res2|res3
    return ans

s1 = {10, 20, 30, 40, 50} 
s2 = {20, 30, 60, 70} 
s3 = {30, 40, 80, 90}
print(find_common(s1,s2,s3)) """