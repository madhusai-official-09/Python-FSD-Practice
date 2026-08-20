# 1.Write a Python program to find the first row containing the maximum number of even elements.
# Input:
# x = [[11, 24, 7, 18],[10, 15, 22, 9],[8, 12, 14, 5],[20, 3, 6, 11]]
# Output:
# [8, 12, 14, 5]
# Even Count: 3

""" x = [[11, 24, 7, 18],[10, 15, 22, 9],[8, 12, 14, 5],[20, 3, 6, 11]]
high = 0
for i in range(len(x)):
    temp = x[i]
    count = 0
    for j in temp:
        if j%2==0:
            count+=1
    if count>high:
        high = count
        a = temp
print(a) """
    

# 2.Write a Python program to find all elements that appear exactly once in the entire nested list, while maintaining their original order.
# Input:
# x = [[10, 20, 30],[20, 40, 50],[30, 60, 70]]
# Output:
# [10, 40, 50, 60, 70]

""" x = [[10, 20, 30],[20, 40, 50],[30, 60, 70]]
y = []
z = []
for i in range(len(x)):
    y.extend(x[i])
for j in y:
    if y.count(j)==1:
        z.append(j)
print(z) """

# 3.Write a Python program to find the row having the maximum difference between its largest and smallest elements.
# Input:
# x = [[10, 25, 18],[5, 40, 12],[30, 35, 20],[8, 50, 15]]
# Output:
# [8, 50, 15]
# Difference: 42

""" x = [[10, 25, 18],[5, 40, 12],[30, 35, 20],[8, 50, 15]]
f = 0
for i in x:
    diff = max(i) - min(i)
    if diff > f:
        f = diff
        a = i
print(a)
print("Difference:",f) """

# 4.Write a Python program to reverse only those tuples whose sum of elements is odd.
# Input:
# x = ((1, 2, 3),(4, 5, 2),(7, 8, 9),(10, 11, 12))
# Output:
# ((1, 2, 3), (2, 5, 4), (7, 8, 9), (12, 11, 10))

""" x = ((1, 2, 3),(4, 5, 2),(7, 8, 9),(10, 11, 12))
output = []
for i in x:
    s = sum(i)
    if s%2!=0:
        a = i[::-1]
        output.append(a)
    else:
        output.append(i)

print(tuple(output)) """

# 5.Write a Python program to find the student who has the highest total marks from a nested dictionary.
# Input:
# students = {"Ravi": {"Math": 85, "Science": 78, "English": 90}, 
#                      "Priya": {"Math": 92, "Science": 88, "English": 84},
#                      "Arjun": {"Math": 76, "Science": 95, "English": 89}}
# Output:
# Student: Priya
# Total Marks: 264

""" students = {"Ravi": {"Math": 85, "Science": 78, "English": 90}, 
                     "Priya": {"Math": 92, "Science": 88, "English": 84},
                     "Arjun": {"Math": 76, "Science": 95, "English": 89}}
t = 0
for i in students:
    total = students[i]["Math"] + students[i]["Science"] + students[i]["English"]
    if total > t:
        t = total
        a = i
print("Student:",a)
print("Total Marks:",t) """

# 6.Write a function that returns True if a number is a Perfect Number, otherwise returns False.
# Input:
# n = 28
# Output:
# True

""" def isperfect(n):
    s = 0
    for i in range(1,(n//2)+1):
        if n%i==0:
            s+=i
    if s == n:
        return True
    else:
        return False
num = 28
ans = isperfect(num)
print(ans) """

# 7.Write a function that takes a number as an argument and returns the number of digits without converting the number into a string.

# Input:
# n = 507080
# Output:
# 6

""" def number_of_digits(num):
    count = 0
    while num>0:
        d = num%10
        count+=1
        num//=10
    return count

n = 507080
ans = number_of_digits(n)
print(ans) """