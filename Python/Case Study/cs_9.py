# 1. Find the first repeated digit without using strings, lists, sets, or dictionaries. 
# Write a Python program using only loops and arithmetic operations to find the first digit that 
# appears more than once, starting from the right side of the number. 
# Input: n = 58374285 
# Output: Repeated digit: 5 

""" n = 58374285
while n>0:
    d = n%10
    n//=10
    while n>0:
        if n%10 == d:
            print("Repeated digit:", d)
            break
        n//=10 """

# 2. Write a Python program to find the saddle point in a given 2D list. 
# A saddle point is an element that is: 
# The smallest element in its row  
# The largest element in its column  
# If a saddle point exists, print the element and its position. Otherwise, print "No Saddle 
# Point". 
# Input: matrix = [[3, 4, 5], 
#                   [2, 6, 8], 
#                   [1, 7, 9]] 
# Output: Saddle Point: 3 
#         Position: (1, 1) 
  
""" m = [[3, 4, 5], 
          [2, 6, 8],
          [1, 7, 9]] """

# 3. Write a recursive function remove_duplicates(s) that removes consecutive duplicate 
# characters from a string without using set() or converting the string into a list. 
# Input: "aaabbccccdaa" 
# Output: "abcda" 

""" def remove_duplicates(s,n_s=""):
    if len(s) == 1:
        return n_s+s[0]
    else:
        first = s[0]
        second = s[1]
        if first!=second:
            n_s+=s[0]
        print(n_s)
        return remove_duplicates(s[1::],n_s)
s = "aaabbccccdaa"
print(remove_duplicates(s)) """

# 4.Create a base class Employee with a method calculate_salary(). 
# Create two child classes: 
# FullTimeEmployee  
# PartTimeEmployee  
# Override calculate_salary() in both classes using different salary calculations. Create objects 
# of both classes and demonstrate polymorphism by calling the same method on both objects. 

