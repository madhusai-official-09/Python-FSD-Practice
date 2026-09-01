# 1. Write a Python program using a closure where the outer function takes a number n and the inner function takes another number x and returns n + x. 
# Input: n = 10 x = 5 
# Output: 15

""" def outerfun(n):
    def innerfun(x):
        return n+x
    return innerfun
res = outerfun(5)
res1= res(10)
print(res1) """

# 2. Create a closure counter() that maintains a count. Every time the inner function is called, it should increase the count by 1 and return the updated count. 
# Input: c = counter() 
# print(c()) print(c()) print(c()) 
# Output: 1 2 3

""" def counter():
    count = 0
    def innerfun():
        nonlocal count
        count+=1
        return count
    return innerfun

c = counter()
print(c())
print(c())
print(c()) """

# 3. Write a closure that stores a number and provides an inner function to increase the stored number by a given value. 
# Input: c = create_counter(10) print(c(5)) print(c(3)) print(c(7)) 
# Output: 15 18 25

""" def create_counter(val):
    def innerfun(val1):
        nonlocal val
        val+= val1
        return val
    return innerfun
c = create_counter(10)
print(c(5))
print(c(3))
print(c(7)) """

# 4. Write a function calculator(n) that returns three inner functions: add(x) → adds x to n sub(x) → subtracts x from n mul(x) → multiplies n by x All three functions must access the same variable n from the outer function. 
# Input: add, sub, mul = calculator(1

""" def calculator(n):
    def addfun(x):
        nonlocal n
        n+=x
        return n
    def subfun(x):
        nonlocal n
        n-=x
        return n 
    def mulfun(x):
        nonlocal n
        n*=x
        return n
    return addfun
c = calculator(5)
print(c(5)) """
            