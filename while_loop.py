# Basic Counting: Write a while loop that counts from 1 to 10 and prints each number.

""" num = 1
while num<=10:
    print(num)
    num += 1 """

# Create a program that asks the user to enter a number, and then use a while loop to count down from that number to 1, printing each value.

# num = int(input("Enter a number: "))
""" while num >=1:
    print(num)
    num -= 1 """

# Write a while loop that calculates the sum of even numbers from 1 to 100.
""" num =  int(input("Enter a number: "))
while num <= 100 and num %2==0 :
    print(num)
    num += num """

# Create a simple number guessing game using a while loop. Generate a random number and have the user guess it, giving hints like "too high" or "too low" until they guess correctly.

""" import random 
random_number = random.randint(1,10)

while True:
    num = int(input("Enter a number: "))
    
    if num < random_number:
        print("too low...")
    elif num > random_number:
        print("too high...")
    else:
        print("Your guess is correct...")
        break """

# Use a while loop to calculate the factorial of a given number.

""" num = int(input("Enter a number: "))
b = 1
count = 1
while b <= num:
    count*=b
    b+=1
print(count) """

# Write a while loop that prints all even numbers between 1 and 50.

""" num = 1
while num<=50:
    if num % 2== 0:
        print(num,end=" ")
    num += 1 """
    
