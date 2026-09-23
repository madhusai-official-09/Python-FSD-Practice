veg = ["potato","onion","tomato"]
quantity = [25,65,40]
price = [18,30,20]

# customer transactions
cart_items=[]
cart_qty=[]
cart_price=[]
while True:
    item = input("What do you want: ")
    if item == "done":
        print(cart_items)
        print(cart_qty,"kgs")
        print(cart_price,"Rs")
        break
    if item in veg:
        qty = int(input("How many kgs: "))
        idx = veg.index(item)
        if qty <=quantity[idx]:
            amt = qty*price[idx]
            cart_items.append(item)
            cart_qty.append(qty)
            cart_price.append(amt)
        else:
            print("Out of stock")
    else:
        print(item,"is not available")