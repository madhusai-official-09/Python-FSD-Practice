# 1. Write a Python program that accepts two integers and performs division.
# If the user enters a non-numeric value, handle the ValueError.
# If the second number is 0, handle the ZeroDivisionError.
# Use try, except, and finally.
# Print the result only when the division is successful.
# Sample Input:
# Enter first number: 25
# Enter second number: 5
# Output:
# Result: 5.0

""" try:
    n = int(input("Enter 1st number: "))
    d = int(input("Enter 2nd number: "))
    ans = n/d
  
except ValueError:
    print("Something Went Wrong.")
except ZeroDivisionError:
    print("it does not accept Zero.")
else:
    print(f"The value is: {ans}")
finally:
    print("The program is closed.") """

        
# 2. Given a matrix, find the sum of the elements present on both diagonals.
# If the matrix has an odd number of rows and columns, do not count the center element twice.
# Input:
# 3 x 3
# 1 2 3
# 4 5 6
# 7 8 9
# Output:
# Diagonal Sum: 25

""" m = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
s=0
for i in range(len(m)):
    s+=m[i][i]
    if i!=len(m)-1-i:
        s+=m[i][len(m)-1-i]
print(f"Diagonal Sum: {s}") """
    
