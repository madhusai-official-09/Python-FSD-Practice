# 1.A movie theater has 20 seats. Seats with numbers divisible by 5 are reserved. Write a program to display only the available seat numbers?

# Input:20
# Output:1 2 3 4 6 7 8 9 11 12 13 14 16 17 18 19

""" seats = int(input("Enter Number of seats: "))
i = 1
while i<=seats:
    if i%5!=0:
        print(i)
    i+=1 """
    
# 2.A company issues employee IDs from 1001 to 1020. Write a program to count how many employee IDs are even?

# Output:10

# Explanation:
# Count the IDs that are divisible by 2.

""" id_start = 1001
id_end = 1020
count = 0
while id_start<=id_end:
    if id_start%2==0:
        count = count + 1
    id_start+=1
print(count) """

# 3.A game contains 15 levels. Bonus rewards are given for levels divisible by 3. Write a program to display all bonus levels?

# Input:15
# Output:3 6 9 12 15

# Explanation:
# Display levels that are divisible by 3.
    

