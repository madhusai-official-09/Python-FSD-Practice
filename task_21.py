# 1. Elements Common in Exactly 2 Sets
# Write a Python program to find the elements that are present in *exactly 2 out of 3 sets*.
# Input:
# A = {1, 2, 3, 4, 5}
# B = {3, 4, 5, 6, 7}
# C = {5, 6, 7, 8, 9}
# Output:
# {3, 4, 6, 7}

""" A = {1, 2, 3, 4, 5}
B = {3, 4, 5, 6, 7}
C = {5, 6, 7, 8, 9}
print((A&B)^(B&C)) """

# 2. Unique Elements After Removing Common Elements
# Write a Python program to find all elements that are present in *only one of the three sets*.
# Input:
# A = {1, 2, 3, 4, 5}
# B = {3, 4, 6, 7}
# C = {4, 7, 8, 9}
# Output:
# {1, 2, 5, 6, 8, 9}

""" a = {1, 2, 3, 4, 5}
b = {3, 4, 6, 7}
c = {4, 7, 8, 9}
print((a|c)^ (b)) """

# 3. Write a Python program to check whether the intersection of two sets forms a sequence of consecutive numbers.
# Input:
# A = {2, 3, 4, 5, 8}
# B = {1, 2, 3, 4, 5}
# Output:
# Consecutive
# Explanation:
# Find the common elements and check whether they form consecutive numbers.

""" A = {2, 3, 4, 5, 8}
B = {1, 2, 3, 4, 5}
ans = (A&B)
temp_list = list(ans)
for i in range(0,len(temp_list)-1):
    temp = temp_list[i]
    next_temp = temp_list[i+1]
    diff = next_temp-temp
    if diff!=1:
        print("Non Consecutive.")
        break
else:
    print("Consecutive.") """
    
# 4. Course Eligibility
# Three sets represent students enrolled in Python, Java, and SQL courses.
# Find the students who are enrolled in both Python and Java but not SQL.
# Input:
# Python = {1, 2, 3, 4, 5, 6}
# Java = {3, 4, 5, 7, 8}
# SQL = {4, 5, 8, 9}
# Output:
# {3}

""" Python = {1, 2, 3, 4, 5, 6}
Java = {3, 4, 5, 7, 8}
SQL = {4, 5, 8, 9}
print((Python&Java)-SQL) """

# 5. Find Exclusive Groups
# Three sets represent employees trained in Python, Java, and SQL.
# Find:
# * Employees trained in *Python and Java but not SQL*
# * Employees trained in *Java and SQL but not Python*
# * Employees trained in *Python and SQL but not Java*
# * Employees trained in *all three*
# Input:
# Python = {1, 2, 3, 4, 5, 6}
# Java = {3, 4, 5, 7, 8}
# SQL = {4, 5, 8, 9}
# Output:
# Python & Java only = {3}
# Java & SQL only = {8}
# Python & SQL only = set()
# All three = {4, 5}

""" Python = {1, 2, 3, 4, 5, 6}
Java = {3, 4, 5, 7, 8}
SQL = {4, 5, 8, 9}
pj = ((Python&Java)-SQL)
js =((Java&SQL)-Python)
ps = ((Python&SQL)-Java)
all = ((Python&Java)&SQL)
print("Python & Java only =",pj)
print('Java & SQL only =',js)
print("Python & SQL only =",ps)
print("All three =",all) """