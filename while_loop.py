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
    
# 7.Create a program that calculates the sum of the digits of a given integer using a while loop.

""" num = int(input("Enter a number: ")) # 5
s = 0
i = 1
while i<=num: 
    s += i 
    
    i += 1 
print(s) """

# 8. Generate a multiplication table for a given number using a while loop.

""" num = int(input("Enter a number: "))
m = 1
while m<=100:
    multi = num * m 
    print(f"{num} X {m} = {multi}")
    m += 1 """
    
# 9. Write a program to find all the factors of a given number using a while loop.

""" num = int(input("Enter a number: "))
d = 1
while d<=num:
    if num%d == 0:
        print(d)
    d+=1 """
     
# 10. Implement a program to reverse a given number using a while loop.

""" num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num%10 
    rev = rev*10+digit
    num = num //10
print(rev) """

# 11. Create a program that prompts the user to enter a password. Keep asking until they enter the correct password.

""" orgpass = "Madhu"
while True:
    passw = input("Enter the password: ")
    if passw == orgpass:
        print("correct")
        break  """
    
