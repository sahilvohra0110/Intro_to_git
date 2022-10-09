

ItemDesc=["","","","",""]
ItemQuantity=[0,0,0,0,0]
ItemValue=[0,0,0,0,0]
ItemCalulatedValue=[""]
Total=0
Adjustment=0

ItemDesc[0]=str(input("Please enter your first item name"))
ItemQuantity[0]=int(input("Please enter your first item quantity"))
ItemValue[0]=int(input("Please enter your first item price"))
ItemCalulatedValue[0]=ItemValue[0]*ItemQuantity[0]

ItemDesc[1]=str(input("Please enter your Second item name"))
ItemQuantity[1]=int(input("Please enter your Second item quantity"))
ItemValue[1]=int(input("Please enter your Second item price"))
ItemCalulatedValue[1]=int(ItemValue[1]*ItemQuantity[1])

ItemDesc[2]=str(input("Please enter your Third item name"))
ItemQuantity[2]=int(input("Please enter your Third item quantity"))
ItemValue[2]=int(input("Please enter your Third item price"))
ItemCalulatedValue[2]=ItemValue[2]*ItemQuantity[2]


Total=ItemCalulatedValue[0]+ItemCalulatedValue[1]+ItemCalulatedValue[2]
Adjustment=Total-(200)

print("Your total price is",Total)
print("You have got a store discount of Rs.200")
print("Your Final amount is",Adjustment)

print("Thank you for shopping with us! Have a great Day")