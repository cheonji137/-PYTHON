price= int(input("Enter the price of the item: "))
if price > 20000:
    shipping_cost = 0
    print("The shipping cost is free.")
elif price < 10000:
    shipping_cost = 3000
    print("The shipping cost is 3000.")
    
print("shipping cost is", shipping_cost)