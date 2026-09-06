# 1. Write a recursive function to find the sum of all even digits in a given number. 
# Input: n = 583624 
# Output: 20

""" def even_digits(n):
    last_digit = n%10
    s = 0
    if last_digit%2 == 0:
        s += last_digit
    if n<10:
        return s
    else:
        return s+even_digits(n//10)

n= 583624
res = even_digits(n)
print(res) """

# 2. Write a recursive function to reverse a given number without using loops or converting the number into a string. 
# Input: n = 48291 
# Output: 19284

""" def rev_num(n,rev=0):
    if n==0:
        return  rev  
    
    rev = rev*10+n%10
    return rev_num(n//10,rev)

n = 48291
res = rev_num(n)
print(res) """

# 3. Write a recursive function to find the factorial of a given number. 
# Input: n = 6 
# Output: 720

""" def factorial(n):
    if n==1:
        return 1
    
    return n*factorial(n-1)

print(factorial(6)) """

# 4. Write a recursive function to find the sum of the first n natural numbers. Input: n = 8 
# Output: 36

""" def sum_natural(n):
    if n== 1:
        return 1
    
    return n+sum_natural(n-1)

print(sum_natural(8)) """

# 5. Write a recursive function to find the nth Fibonacci number. 
# Input: n = 7 
# Output: 13

""" def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(7)) """