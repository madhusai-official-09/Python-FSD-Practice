# 1. Basic Counting: Write a while loop that counts from 1 to 10 and prints each number.

""" num = 1
while num<=10:
    print(num)
    num += 1 """

# 2. Create a program that asks the user to enter a number, and then use a while loop to count down from that number to 1, printing each value.

# num = int(input("Enter a number: "))
""" while num >=1:
    print(num)
    num -= 1 """

#3. Write a while loop that calculates the sum of even numbers from 1 to 100.
""" num =  int(input("Enter a number: "))
sum = 0
while num<=100:
    sum+=num
    num += 2
print(sum) """

# 4. Create a simple number guessing game using a while loop. Generate a random number and have the user guess it, giving hints like "too high" or "too low" until they guess correctly.

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

# 5. Use a while loop to calculate the factorial of a given number.

""" num = int(input("Enter a number: "))
b = 1
count = 1
while b <= num:
    count*=b
    b+=1
print(count) """

# 6. Write a while loop that prints all even numbers between 1 and 50.

""" num = 1
while num<=50:
    if num % 2== 0:
        print(num,end=" ")
    num += 1 """
    
# 7.Create a program that calculates the sum of the digits of a given integer using a while loop.

""" num = int(input("Enter a number: ")) 
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print(sum) """

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
    
# 12. Write a program using a while loop to generate the first n terms of the Fibonacci sequence.

""" num = int(input("Enter a number: "))

a = 0
b = 1
count = 1

while count<=num:
    print(a)
    temp = a + b
    a = b
    b = temp
    count += 1  """

# 13. Build a program that checks if a given number is prime using a while loop.

""" num = int(input("Enter a number: "))
d = 2
while d<=num//2:
    if num%d==0:
        print("Not Prime...")
        break
    d = d+1
else:
    print("Prime...") """
    
# 14. Create a program that checks if a given word or phrase is a palindrome (reads the same forwards and backwards) using a while loop.

""" word = input("Enter Word: ")
rev = ""
i = len(word) - 1
while i>=0:
    rev += word[i]
    i-=1
if rev == word:
    print("Palindrome...")
else:
    print("Not Palindrome...")
 """


# 15. Write a program to generate the first n rows of Pascal's Triangle using while loops.




# 16. Create a program that converts a given integer into words (e.g., 123 -> "one hundred twenty-three") using a while loop.

# 17. Write a program to reverse a given string using a while loop.

# 18. Implement a program to find the greatest common divisor of two numbers using a while loop and the Euclidean algorithm.

# 19. Create a program that converts a binary number (entered as a string) to its decimal equivalent using a while loop

# 20. Write a program that prints all prime numbers between 1 and 100 using a while loop

""" num = 2
while num<=100:
    d = 2
    while d<=num//2:
        if num%d==0:
            break
        d+=1
    else:
        print("Prime", num)
    num+=1 """


n =  int(input("Enter n value: ")) # 1
cnt  = 0
a = 0
b = 1
while True:
    c = a + b # 0+1 -> c = 1 , c = 2
    if c>1: # 1>1 -> F , 2>1 -> T
        d = 2 
        while d<=c//2: # 2<=2//2 -> 2<=1 -> F
            if c%d==0: 
                break
            d+=1
        else:
            cnt  = cnt+1 # cnt = 1
            if cnt == n: # 1 == 1
                print(c) # 2
                break
    a = b # a = 1
    b = c # b = 1
    
