# x = int(input("Enter a number: "))
# if not x%2==1:
#     print("Even")
# else:
#     print("Odd")

# x= int(input("Enter a Number: "))
# if not(x%3==0 or x%7==0):
#     print("Chiranjeevi")
# else:
#     print("Balayya")

# num = int(input("Enter a number: "))
# if num>0:
#     print("Possitive")
# elif num<0:
#     print("Negative")
# else:
#     print("Zero")

# ---Fizz Buzz Game---

# num = int(input("Enter a number: "))
# if num %3==0 and num%5==0:
#     print("FizzBuzz")
# elif num%3==0:
#     print("Fizz")
# elif num%5==0:
#     print("Buzz")
# else:
#     print("Invalid")

# ---Biggest in given 2 Numbers---
# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# if num1>num2:
#     print("Biggest is: ",num1)
# else:
#     print("Biggest is: ",num2)

# Leap year or Not

# year = int(input("Enter a year: "))
# if (year%4==0 and year%100!=0) or (year%400==0):
#     print("Leap Year")
# else:
#     print("Not Leap year")

# customer discount

price = int(input("Enter price: "))
membership = input("Enter you have membership or not: yes|no : ")
coupon = input("Enter if you have coupon: yes|no : ")
ans = 0 
if price > 1000:
    ans = ans+ (10/100)*price
if membership == "yes":
    ans +=  (5/100)*price
if coupon == "yes":
    ans +=(6/100)*price
else:
    print("No Discount")
print(price - ans)



