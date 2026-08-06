# 1. Write a Python program to print the list starting from the second element up to the second last element, taking every third element using slicing.

# Input:
# [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Output:
# [20, 50, 80]

""" li  = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n_li = li[1:len(li):3]
print(n_li) """

# 2. Write a Python program to print the list from the third last element to the beginning in reverse order using slicing.

# Input:
# [10, 20, 30, 40, 50, 60, 70, 80]

# Output:
# [60, 50, 40, 30, 20, 10]

""" li  = [10, 20, 30, 40, 50, 60, 70, 80]
n_li = li[-3::-1]
print(n_li) """

# 3. Write a Python program to divide the given list into two equal halves and swap the halves using slicing.

# Input:
# [10, 20, 30, 40, 50, 60, 70, 80]

# Output:
# [50, 60, 70, 80, 10, 20, 30, 40]

""" li  = [10, 20, 30, 40, 50, 60, 70, 80]
mid = len(li)//2
n_li = li[mid::] + li[:mid]
print(n_li) """

# 4. Write a Python program to reverse only the second half of the given list using slicing.

# Input:
# [10, 20, 30, 40, 50, 60, 70, 80]

# Output:
# [10, 20, 30, 40, 80, 70, 60, 50]

""" li = [10, 20, 30, 40, 50, 60, 70, 80]
mid = len(li)//2
n_li = li[:mid] + li[mid:][::-1]
print(n_li) """

# 5. Write a Python program to rotate the given list to the right by K positions using slicing.

# Input:
# List: [10, 20, 30, 40, 50, 60, 70, 80]
# K = 3

# Output:
# [60, 70, 80, 10, 20, 30, 40, 50]

""" li = [10, 20, 30, 40, 50, 60, 70, 80]
k = 3
mid = len(li) - k
n_li= li[mid::] + li[:mid]
print(n_li) """

                       # List Comprehension Problems
# 6. Write a Python program using List Comprehension to create a new list containing the square of all even numbers from the given list.

# Input:
# [2, 3, 4, 5, 6, 7, 8]

# Output:
# [4, 16, 36, 64]

""" li = [2, 3, 4, 5, 6, 7, 8]
n_li = [i**2 for i in li if i%2==0]
print(n_li) """

# 7. Write a Python program using List Comprehension to create a new list containing only the numbers whose last digit is 5.

# Input:
# [12, 25, 35, 41, 55, 60, 75]

# Output:
# [25, 35, 55, 75]

""" li = [12, 25, 35, 41, 55, 60, 75]
n_li = [i for i in li if i%10 == 5 ]
print(n_li) """

seats = ["Gold",]
for seat in seats:
    add_seat = input("Enter: ")
    seats.append(add_seat)
    break
print(seats)