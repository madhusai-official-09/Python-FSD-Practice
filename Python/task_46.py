# 1. Write a Python program that accepts employee names and their salaries. Display the employee with the highest salary, the employee with the lowest salary, and the average salary. Also display the employees whose salary is greater than the average salary.
# Input: Names: Ravi, Priya, Arun, Sneha
#             Salaries: 35000, 42000, 28000, 50000
# Output:        Highest Salary: Sneha – 50000
#                Lowest Salary: Arun – 28000
#                Average Salary: 38750
#                Above Average: Priya, Sneha

""" names = ["Ravi", "Priya", "Arun", "Sneha"]
salaries = [35000, 42000, 28000, 50000]
total = 0
highest = salaries[0]
lowest = salaries[0]
for i in range(len(salaries)):
    total += salaries[i]
    
    if salaries[i]>highest:
        highest = salaries[i]
    if salaries[i]<lowest:
        lowest = salaries[i]
        
avg = total/len(salaries)
print(f"Average Salary: {avg}")

for i in range(len(salaries)):
    if salaries[i] == highest:
        print(f"Highest Salary: {names[i]} - {highest}")
    if salaries[i] == lowest:
        print(f"Lowest Salary:{names[i]} - {lowest}")
    
    if salaries[i]>avg:
        print(f"Above Average: {names[i]}") """
        
# 2.Write a Python program using multiple decorators for a function calculate_bill(amount).
# check_amount decorator should check whether the amount is greater than 0.
# add_tax decorator should add 18% GST to the amount.
# show_result decorator should display the final bill amount.
# Apply all three decorators to the function.
# Input:
# amount = 1000

# Expected Output:
# Original Amount: 1000
# GST: 180.0
# Final Bill: 1180.0

""" def check_amount(func):
    def fun(amount):
        if amount <= 0:
            print("Amount should be greater than 0")
        else:
            func(amount)
    return fun

def add_tax(func):
    def fun(amount):
        gst = amount * 0.18
        final_amount = amount + gst
        print(f"Original Amount: {amount}")
        print(f"GST: {gst}")
        func(final_amount)
    return fun

def show_result(func):
    def fun(amount):
        print(f"Final Bill: {amount}")
    return fun
@check_amount
@add_tax
@show_result
def calculate_bill(amount):
    print(f"Final Bill: {amount}")
    
amount = 1000
calculate_bill(amount) """

# 3.Given two matrices, write a Python program to find their sum and then find the largest element in the resulting matrix.
# Input:
# Output:
# Sum Matrix:
# [3, 6, 9]
# [5, 8, 11]
# [9, 9, 12]
# Largest Element: 12
"""
m1 = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]
m2 = [
    [1, 2, 3],
    [4, 5, 6],
    [2, 1, 3]
]

m3 = []

if len(m1) == len(m2):
    result = []
    for i in range(len(m1)):
        row = []
        for j in range(len(m1[i])):
            row.append(m1[i][j] + m2[i][j])
        result.append(row)
        m3.append(row)
print("Sum Matrix:")
for row in result:
    print(row) """
        
