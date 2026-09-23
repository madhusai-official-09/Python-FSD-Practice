# 1. Write a generator function that takes a number and generates its digits from right to left. 
# Input: n = 58321 
# Output: 1 2 3 8 5

""" def generator_digits(n):
    while n>0:
        d = n%10
        yield d
        n=n//10
       
n = 58321
for i in generator_digits(n):
    print(i) """
    
# 2. Write a generator function that generates the first n Fibonacci numbers. 
# Input: n = 7 
# Output: 0 1 1 2 3 5 8

""" def fibonacci(n):
    a = 0
    b = 1
    print(a)
    print(b)
    i = 3
    while i<=n:
        c=a+b
        yield c
        i+=1
        a=b
        b=c  
n = 7
for i in fibonacci(n):
    print(i) """
    
# 3. Write a generator function that takes a list and yields an element only when it is different from the previously yielded element. 
# Input: nums = [1, 1, 2, 2, 2, 3, 1, 1, 4] 
# Output: 1 2 3 1 4

""" def list(nums):
    for i in range(len(nums)):
        if nums[i]!=nums[i-1]:
            yield nums[i]
            
li = [1, 1, 2, 2, 2, 3, 1, 1, 4] 
for i in list(li):
    print(i) """
    
# 4. Write a generator function that generates the first n prime numbers. 
# Input: n = 8 
# Output: 2 3 5 7 11 13 17 19

""" def isprime(n):
    prime_count = 0
    i=2
    while True:
        num = i
        for j in range(2, (num//2)+1):
            if num%j==0:
                break
        else:
            yield num
            prime_count+=1
        if prime_count == n:
            break
        i+=1
n = 8
for i in isprime(n):
    print(i) """
    
# 5. Write a Python generator function that takes a compressed string and yields each character/group according to its count. 
# Input: a[2]bc[3] 
# Output: a a bc bc bc

""" def decompress_string(st):
    i = 0
    while i < len(st):
        if st[i].isalpha():
            yield st[i]
            i += 1
        elif st[i] == '[':
            count = ''
            j = i + 1
            while j < len(st) and st[j] != ']':
                count += st[j]
                j += 1
            count = int(count)
            content = st[i - 1]
            for _ in range(count):
                yield content
            i = j + 1
        else:
            i += 1
s = "a[2]bc[3]"
for i in decompress_string(s):
    print(i) """
        