# 1. Write a recursive function reverse_number(n) to reverse a given number without converting it into a string and without using loops. 
# Input: n = 123450 
# Output: Reverse = 54321

""" def reverse_number(n,rev = 0):
    if n == 0:
        return rev
    else:
        d = n%10
        rev = rev*10+d
        n//=10
        return reverse_number(n,rev)
    
print(reverse_number(123450)) """

# 2. Write a Python program to find the student who scored the highest total marks using a nested dictionary. 
# Input: students = { "S1": {"name": "Ravi", "marks": {"Python": 85, "SQL": 78, "Django": 90}}, "S2": {"name": "Anu", "marks": {"Python": 92, "SQL": 88, "Django": 95}}, "S3": {"name": "Kiran", "marks": {"Python": 80, "SQL": 75, "Django": 85}} } 
# Output: Student with highest total marks: Anu

students = { "S1": {"name": "Ravi", "marks": {"Python": 85, "SQL": 78, "Django": 90}}, "S2": {"name": "Anu", "marks": {"Python": 92, "SQL": 88, "Django": 95}}, "S3": {"name": "Kiran", "marks": {"Python": 80, "SQL": 75, "Django": 85}} }
n = ""
for i in students:
    total = sum(students[i]["marks"].values())
    students[i]["total"] = total
