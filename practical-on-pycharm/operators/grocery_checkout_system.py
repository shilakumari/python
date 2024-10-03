#Grocery checkout:
#Input:
#3 Items
#Enter item name and quantity
#Subtotal
#8.5 % Tex
# Total_amount

#dictionary
prices={
    "apple":0.30,
    "banana":0.50,
    "milk":1.20,
    "bread":1.30,
    "cheese":2.30
}
item1_name=input("Enter the name of the first item").lower()
item1_qty=int(input(f"Enter the quantity of {item1_name}"))

item2_name=input("Enter the name of the second item").lower()
item2_qty=int(input(f"Enter the quantity of {item2_name}"))

item3_name=input("Enter the name of the third item").lower()
item3_qty=int(input(f"Enter the quantity of {item3_name}"))

#price
item1_price=prices.get(item1_name,0)
item2_price=prices.get(item2_name,0)
item3_price=prices.get(item3_name,0)

item1_total=item1_price*item1_qty
item2_total=item2_price*item2_qty
item3_total=item3_price*item3_qty

sub_total=item1_total+item2_total+item3_total
tax=float(sub_total)*0.085
total_amount=sub_total+tax

print("----Receipt----")
print(f"{item1_name.capitalize()}: {item1_qty} @ ${item1_price:.2f} each = ${item1_total:.2f}")
print(f"{item2_name.capitalize()}: {item2_qty} @ ${item2_price:.2f} each = ${item2_total:.2f}")
print(f"{item3_name.capitalize()}: {item3_qty} @ ${item3_price:.2f} each = ${item3_total:.2f}")


