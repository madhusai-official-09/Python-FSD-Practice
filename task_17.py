# 1.Write a Python program to print all elements that are greater than both of their adjacent elements.
# Input:
# [5, 18, 10, 25, 15, 30, 20]
# Output:
# 18 25 30

""" li = [5, 18, 10, 25, 15, 30, 20]
x =0 
left = 0
right = 1
while x<len(li)-1:
    if li[left]<li[right]:
        print(li[right])
    left+=1
    right+=1
    x+=1 """
    
# 2.Write a Python program to print all elements in a list that are equal to the sum of all previous elements.
# Input:
# [2, 3, 5, 10, 20, 21]
# Output:
# 5 10 20
# Explanation:
# 5 = 2 + 3
# 10 = 2 + 3 + 5
# 20 = 2 + 3 + 5 + 10

""" li = [2, 3, 5, 10, 20, 21]
s = 0
for i in li:
    if s==i:
        print(i)
    s+=i """
    
# 3.Write a Python program to split a list into groups of 3 elements using slicing and print only the groups whose sum is greater than 50.
# Input:
# [10, 20, 30, 5, 10, 15, 25, 20, 15]
# Output:
# [10, 20, 30]
# [25, 20, 15]

li = [10, 20, 30, 5, 10, 15, 25, 20, 15]
n_li = []
for i in range(0,len(li),3):
    if 
 
   
# 4.Write a Python program using List Comprehension to create a new list containing the square of all even numbers.
# Input:
# [2, 3, 4, 5, 6, 7]
# Output:
# [4, 16, 36]

""" li = [2, 3, 4, 5, 6, 7]
n_li = [i**2 for i in li if i%2==0]
print(n_li) """

# 5.Write a Python program using List Comprehension to create a new list containing the squares of the numbers that are divisible by 5.
# Input:
# [5, 8, 10, 12, 15, 18, 20]
# Output:
# [25, 100, 225, 400]

""" li = [5, 8, 10, 12, 15, 18, 20]
n_li = [i**2 for i in li if i%5==0]
print(n_li) """

# 6.Write a Python program using List Comprehension to create a new list containing only the perfect square numbers from the given list.
# Input:
# [4, 7, 9, 10, 16, 18, 25]
# Output:
# [4, 9, 16, 25]

""" li = [4, 7, 9, 10, 16, 18, 25]
n_li = [i for i in li if (i**0.5)**2==i]
print(n_li) """

# 7.Write a Python program using List Comprehension to create a new list containing the cubes of all odd numbers.
# Input:
# [2, 3, 4, 5, 6, 7]
# Output:
# [27, 125, 343]

""" li = [2, 3, 4, 5, 6, 7]
n_li = [i**3 for i in li if i%2!=0]
print(n_li) """
        
    