# 1. Write a Python program using lambda and map() to replace every number in a list with its square. 
# Input: lst = [2, 4, 6, 8, 10] 
# Output: [4, 16, 36, 64, 100]

""" lst = [2, 4, 6, 8, 10]
ans = list(map(lambda n: n**2,lst))
print(ans) """

# 2. Write a Python program using lambda and filter() to extract all numbers that are divisible by both 3 and 5. 
# Input: lst = [10, 15, 20, 30, 45, 50, 60, 72] 
# Output: [15, 30, 45, 60]

""" lst = [10, 15, 20, 30, 45, 50, 60, 72]
ans = list(filter(lambda n: n%3==0 and n%5==0,lst))
print(ans) """

# 3. Write a Python program using lambda and reduce() to find the product of all numbers in a list. 
# Input: lst = [2, 3, 4, 5] 
# Output: 120

""" from functools import reduce
lst = [2, 3, 4, 5]
ans = reduce(lambda a,b:a*b,lst)
print(ans) """

# 4. Write a Python program using lambda, filter(), and map() to select all even numbers from a list and then find their cubes. 
# Input: lst = [1, 2, 3, 4, 5, 6, 7, 8] 
# Output: [8, 64, 216, 512]

""" lst = [1, 2, 3, 4, 5, 6, 7, 8]
ans = list(map(lambda n:n**3,filter(lambda n:n%2==0,lst)))
print(ans) """

# 5. Create a class Student with the attributes name and marks. Create an object and display the student's details. 
# Input: name = "Rahul" marks = 85 
# Output: Name: Rahul Marks: 85

""" class Student:
    def __init__(self,n,m):
        self.name = n
        self.marks = m
    def display(self):
        print(f"Name: {self.name}")
        print(f"Marks: {self.marks}")
        
s1=Student("Rahul",85)
s1.display() """