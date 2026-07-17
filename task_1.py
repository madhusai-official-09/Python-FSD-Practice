# 1. Write a Python program to determine the *shipping charge* based on the order amount.
#    *Input:* Order Amount = ₹1800
#    *Output:* Shipping Charge = ₹50

#    *Conditions:*

#    * Below ₹500 → ₹100
#    * ₹500 to ₹1999 → ₹50
#    * ₹2000 and above → Free Shipping

""" order_amount = int(input("Enter order_amount: "))
if order_amount < 500:
    print("Shipping Charge -> ₹100")
elif order_amount >= 500 and order_amount <= 1999:
    print("Shipping Charge -> ₹50")
else:
    print("Free Shipping...") """
    
# 2. Write a Python program to determine the *membership level* based on reward points.
#    *Input:* Reward Points = 850
#    *Output:* Gold Member

#    *Conditions:*

#    * Below 200 → Bronze
#    * 200 to 499 → Silver
#    * 500 to 999 → Gold
#    * 1000 and above → Platinum

""" reward_points = int(input("Enter reward_points: "))
if reward_points<200:
    print("Bronze Member.")
elif reward_points>=200 and reward_points<=499:
    print("Silver Member.")
elif reward_points>=500 and reward_points<=999:
    print("Gold Member.")
else:
    print("Platinum Member.") """
    
# 3. Write a program to calculate the sum of the first N natural numbers using a while loop.
# Input:10
# Output:55

""" num = int(input("Enter a number: "))
sum = 0
d = 1
while d<=num:
    sum+=d
    d+=1
print("First N natural numbers is:",sum) """

# 4.Write a program to find the product of all odd numbers from 1 to N using a while loop.
# Input:10
# Output:945

""" num = int(input("Enter a number: "))
b = 1
count = 1
while b<=num:
    if b%2==1:
        count*=b
    b+=1
print(count) """

# 5.Write a Python program to check whether a number is Prime or not using a while loop.
# Input:17
# Output: Prime Number

""" num = int(input("Enter a number: "))#4
d = 1
while d<=num//2:#1<=3//2 -> T
    if num%2==0: # 2%2==0 -> T
        print("Not Prime...") # ->T
        break
    d+=1
else:
    print("Prime...") """
 
# 6.write a python program to Print numbers divisible by both 2 and 3 using while loop.
# Input:20
# Output:6 12 18

""" num = int(input("Enter a Number: "))
count = 1
sum = 0
while count<=num:
    if count%2==0 and count%3==0:
        print(count)
    count+=1 """
    
    
# ATM Machine

pin =1234
show_menu = False
count = 1
while count<=3:
    mypin = int(input("Enter your pin: "))
    if mypin == pin:
        print("Valid Pin")
        show_menu = True
        break
    else:
        print("Invalid Pin")
    count+=1
else:
    print("Card Blocked")

if show_menu == True:
    
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    
    ch = int(input("Enter your Choice(1/2/3/4): "))