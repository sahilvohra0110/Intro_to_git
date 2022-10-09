from ast import If

n=int(input("Enter no of items"))


c=ItemName=str(input("Please enter your item name"))
ItemQuantity=int(input("Please enter item quantity"))
if ItemName == str("Pizza"):
    TotalPriceOfItem=ItemQuantity*200
    print(TotalPriceOfItem)

elif ItemName == str("Burger"):
    TotalPriceOfItem=ItemQuantity*90
    print(TotalPriceOfItem)

elif ItemName == str("Momos"):
    TotalPriceOfItem=ItemQuantity*50
    print(TotalPriceOfItem)
