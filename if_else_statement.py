# 1. Write a Python program that checks if a given year is a leap year.
""" year = int(input("Enter a year:"))
res = "Leap Year" if (year%4==0 and year%100!=0) or (year%400==0) else "Not a leap year"
print(res) """ 

# 2. Write a Python program that checks if a given character is a vowel or a consonant.

""" ch = input("Enter a character: ")
if ch in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
    print("The character is a vowel.")
else:
    print("The character is a consonant.") """
    
# 3. Write a Python program that checks if a given year is a century year (ending in '00').

""" year = int(input("Enter Year: "))
if year%100==0:
    print("Century year ->",year)
else:
    print("Not a century year") """
    
# 4. Write a Python program that checks if a given number is prime.
num = int(input("Enter a Number: "))
d = 2
while d<=num//2:
    if num%d==0:
        print("Not a Prime...")
        break
    d+=1
else:
    print("Prime ->",num)
    
# 5. Write a Python program that checks if a person is eligible to vote based on their age.
""" age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.") """
    
# 6. Write a Python program that checks if a number is positive or non-positive(including zero).
""" num = int(input("Enter a number: "))
if num>0:
    print("Positive")
else:
    print("Negative") """
    
# 7. Write a Python program that compares two numbers and prints the largest one.
""" n1 = int(input("Enter 1st Number: "))
n2 = int(input("Enter 2nd Number: "))
if n1>n2:
    print(n1)
else:
    print(n2) """
    