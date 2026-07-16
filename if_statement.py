# 1. Write a Python program that checks if a number is positive.
""" num = int(input("Enter a number: "))
if num>0:
    print("Positive Number") """

# 2. Write a Python program that checks if a given string is empty.
""" string = input("Enter a string: ")
if string == (""):
    print("empty") """

# 3. Write a Python program that determines if a number is positive, negative, or zero using only if statements and no elif or else.

""" num = int(input("Enter a number: "))
if num >0:
    print("Positive")
if num<0:
    print("Negative")
if num==0:
    print("Zero") """

# 4. Write a Python program that checks if a number is a multiple of both 3 and 5.
""" num =int(input("Enter a number: "))
if num%3==0 and num%5==0:
    print(num) """

# 5. Write a Python program that determines if a given number is a perfect square.
""" num =int(input("Enter a number: "))
root = int(num**0.5)
if root * root == num:
    print("Perfect Square: ",num) """

# 6. Write a Python program that checks if a number is divisible by both 2 and 3.
""" num = int(input("Enter a number:"))
if num%2==0 and num%3==0:
    print(num," is divisible by both 2 and 3") """

# 7. Write a Python program that determines if a number is a perfect cube.
""" num = int(input("Enter a number: "))
root = num**(1/3)
if num == root**3:
    print(num,"is a Perfect Cube") """

# 8. Write a Python program that checks if a given number is a multiple of 4.
""" num = int(input("Enter a number: "))
if num % 4 == 0:
    print(num,"is a multiple of 4.") """