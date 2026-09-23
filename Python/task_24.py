# 1.Write a Python program to Most Frequent Word.
# Input
# ["apple","banana","apple","orange","banana","banana"]
# Output
# banana

""" d = ["apple","banana","apple","orange","banana","banana"]
f = 0
for i in d:
    cnt = d.count(i)
    if cnt>f:
        f = cnt
        word = i 
print(word) """

# 2.Seats are booked.
# If the same seat is booked again, ignore it.
# bookings = 10,5,8,5,12,8,11,5
# Print only successful bookings.

""" bookings = 10,5,8,5,12,8,11,5
f = []
for i in bookings:
    if i not in f:
        f.append(i)
print(*f) """

# 3.Write a Python program to create a new dictionary containing only employees whose salary is greater than ₹40,000.
# Input:
# employees = {
#     "Ravi": 30000,
#     "Anil": 45000,
#     "Kiran": 50000,
#     "Suresh": 35000
# }
# Output:
# {
#     "Anil": 45000,
#     "Kiran": 50000
# }

""" employees = {
    "Ravi": 30000,
    "Anil": 45000,
    "Kiran": 50000,
    "Suresh": 35000
}
output = {}
for i  in employees:
    if employees[i]>40000:
        output[i] = employees[i]
print(output) """

# 4.Write a Python program to find the employee who receives the highest salary.
# Input:
# employees = {
#     "E101": {
#         "name": "Ravi",
#         "salary": 35000
#     },
#     "E102": {
#         "name": "Anil",
#         "salary": 50000
#     },
#     "E103": {
#         "name": "Kiran",
#         "salary": 45000
#     }
# }
# Output:
# Anil

""" employees = {
    "E101": {
        "name": "Ravi",
        "salary": 35000
    },
    "E102": {
        "name": "Anil",
        "salary": 50000
    },
    "E103": {
        "name": "Kiran",
        "salary": 45000
    }
}
high_salary = 0
for i in employees:
    if employees[i]["salary"] > high_salary:
        high_salary = employees[i]["salary"]
        high_name = employees[i]["name"]
print(high_name) """

# 5.A student dictionary contains marks for multiple subjects. Write a Python program to calculate the total marks of each student.
# Input:
# students = {
#     "Ravi": {
#         "Python": 80,
#         "Java": 75,
#         "SQL": 85
#     },
#     "Anil": {
#         "Python": 90,
#         "Java": 85,
#         "SQL": 88
#     }
# }
# students = {
#     "Ravi": {
#         "Python": 80,
#         "Java": 75,
#         "SQL": 85
#     },
#     "Anil": {
#         "Python": 90,
#         "Java": 85,
#         "SQL": 88
#     }
# }
# Output:
# Ravi: 240
# Anil: 263

""" students = {
    "Ravi": {
        "Python": 80,
        "Java": 75,
        "SQL": 85
    },
    "Anil": {
        "Python": 90,
        "Java": 85,
        "SQL": 88
    }
}
output = {}
for i in students:
    total = students[i]["Python"] + students[i]["Java"] + students[i]["SQL"]
    output[i] = total
print(output) """
    