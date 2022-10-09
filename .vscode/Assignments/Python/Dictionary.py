items=[{"ItemName":"",
"ItemQuantity":"",
"ItemPrice":"",
"ItemTotal":""},
{"ItemName":"",
"ItemQuantity":"",
"ItemPrice":"",
"ItemTotal":""},
{"ItemName":"",
"ItemQuantity":"",
"ItemPrice":"",
"ItemTotal":""},
{"ItemName":"",
"ItemQuantity":"",
"ItemPrice":"",
"ItemTotal":""},
{"ItemName":"",
"ItemQuantity":"",
"ItemPrice":"",
"ItemTotal":""}]

print("Welcome to python super market!! Let's start billing your items")

items[0]["ItemName"]=str(input("Please enter the item name : "))
items[0]["ItemQuantity"]=int(input("Please enter the item Quantity : "))
items[0]["ItemPrice"]=int(input("Please enter the item Price : "))
items[0]["ItemTotal"]=items[0]["ItemQuantity"]*items[0]["ItemPrice"]

print("Your total price of first item is", items[0]["ItemTotal"])

items[1]["ItemName"]=str(input("Please enter the item name : "))
items[1]["ItemQuantity"]=int(input("Please enter the item Quantity : "))
items[1]["ItemPrice"]=int(input("Please enter the item Price : "))
items[1]["ItemTotal"]=items[1]["ItemQuantity"]*items[1]["ItemPrice"]

print( "Your total price of Second item is", items[1]["ItemTotal"])

items[2]["ItemName"]=str(input("Please enter the item name : "))
items[2]["ItemQuantity"]=int(input("Please enter the item Quantity : "))
items[2]["ItemPrice"]=int(input("Please enter the item Price : "))
items[2]["ItemTotal"]=items[2]["ItemQuantity"]*items[2]["ItemPrice"]

print( "Your total price of Third item is", items[2]["ItemTotal"])

items[3]["ItemName"]=str(input("Please enter the item name : "))
items[3]["ItemQuantity"]=int(input("Please enter the item Quantity : "))
items[3]["ItemPrice"]=int(input("Please enter the item Price : "))
items[3]["ItemTotal"]=items[3]["ItemQuantity"]*items[3]["ItemPrice"]

print( "Your total price of Fourth item is", items[3]["ItemTotal"])

items[4]["ItemName"]=str(input("Please enter the item name : "))
items[4]["ItemQuantity"]=int(input("Please enter the item Quantity : "))
items[4]["ItemPrice"]=int(input("Please enter the item Price : "))
items[4]["ItemTotal"]=items[4]["ItemQuantity"]*items[4]["ItemPrice"]

print( "Your total price of Fifth item is", items[4]["ItemTotal"])

OverallTotal=items[1]["ItemTotal"]+items[2]["ItemTotal"]+items[3]["ItemTotal"]+items[4]["ItemTotal"]+items[0]["ItemTotal"]

print("Your overall total value for these 5 items are", OverallTotal)

StoreDiscount=OverallTotal*(0.08)

print("Your store offer of 8% will be", StoreDiscount)

GST=((OverallTotal)-(StoreDiscount))*(0.18)

print("Your total GST is", GST)

BillingAmount= ((OverallTotal)-(StoreDiscount))-(GST)

print("Your final billing amount is",BillingAmount)

print("Thank you for shopping with us, Have a great Day!!!!")