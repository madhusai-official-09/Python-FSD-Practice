# 1. Given a list of integers, display the elements whose indexes are both prime numbers and Fibonacci numbers. Input: [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] Output: 20 30 50

""" def isprime(n):
    if n<=1:
        return False
    else:
        for d in range(2,(n//2)+1):
            if n%d==0:
                return False
        else:
            return True
def isfibonacci(n):
    if n==0 or n==1:
        return True
    else:
        a = 0
        b = 1
        c = a+b
        while c<n:
            a = b
            b = c
            c = a+b
        if c==n:
            return True
        else:
            return False
    
def prime_fib(li,n_li=[]):
    for i in range(len(li)):
        j = i+1
        p = isprime(j)
        f = isfibonacci(j)
        if p == True and f == True:
            n_li.append(li[i])
    return n_li

li = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
ans = prime_fib(li)
print(ans) """

# 2. Write a function max_after_removal(n, digit) that removes one occurrence of the given digit from the number and returns the maximum possible number.

# If the digit occurs multiple times, try removing it from each occurrence and find which removal produces the largest number.

# Input:

# n = 154325
# digit = 5

# Possible numbers:

# 14325   # remove the first 5
# 15432   # remove the second 5

# Output:

# 15432

def max_after_removal(n, d):
    

    