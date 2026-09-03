# 1. Write a Python program using a decorator to display a message before and after executing the function. 
# Input: hello batch 89 
# Output: Function Started hello batch 89 Function Ended

""" def dec(fun):
    def inner(*args):
        print("Function Started")
        fun(*args)
        print("Function Ended")
    return inner

@dec
def greet(name):
    print(name)
greet("hello batch 89") """


# 2. Write a Python program using a decorator to count the number of times a function is called. 
# Input: hello() hello() hello() 
# Output: Call 1: hello Call 2: hello Call 3: hello

""" def dec_count(fun):
    count = 0
    def inner():
        nonlocal count
        count+=1
        print(f"Call {count}: ",end="")
        fun()
    return inner

@dec_count
def hello():
    print("hello")
hello()
hello()
hello() """

# 3. Write a Python program using a decorator to display a message before adding two numbers. 
# Input: n1 = 10 n2 = 20 
# Output: Adding 10 and 20 Sum = 30

""" def add(fun):
    def inner(n1,n2):
        ans = fun(n1,n2)
        res = f"Adding {n1} and {n2} Sum = {ans}"
        return res
    return inner
@add
def calculate(n1,n2):
    return n1+n2

print(calculate(10,20)) """

# 4. Write a Python program using a decorator to multiply the return value of a function by 2. 
# Input: calculate(5) 
# Output: Original Result: 5 Final Result: 10

""" def multiply(fun):
    def inner(n):
        ans = fun(n)
        res = f"Original Result: {ans} Final Result: {ans*2}"
        return res
    return inner

@multiply
def calculate(n):
    return n

print(calculate(5)) """


# 5. Write a Python program using two decorators. The first decorator should convert the message to uppercase, and the second decorator should add !!! at the end. Input: hello batch 89 
# Output: HELLO BATCH 89!!!

""" def uppercase(fun):
    def inner(s): 
        res= fun(s)
        return res.upper()
    return inner

def add(fun):
    def inner(s):
        res=fun(s)
        ans = f"{res}!!!"
        print(ans)
    return inner
        
@add
@uppercase
def ch(s):
    return s
s = "hello batch 89"
ch(s) """