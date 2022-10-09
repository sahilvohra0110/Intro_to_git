from typing import List


f=open("bill.csv", "a")

f.write("Customer_name,Mobile_no,itemID,qty,total")
f.write("\n")
customer_name = input("Please enter your name")
mobile_no = input("Please enter your mob no")
prodfile= open("prodlist.csv", "r")
#to display the item list and price
for x in prodfile:
    print(x)
prodfile.close()
item_ID = input("Please enter the item id")
qty= int(input("Please enter the quantity of item"))
#getting the item unit price
prodfile= open("prodlist.csv", "r")
p=[]
for x in prodfile:
    print(x)
    proditem=x.split(",")
    # print(proditem[0])
    # p= p.append(proditem[0])
    # print(proditem[2])
    if proditem[0]== item_ID:
        unitPrice= proditem[2]
        break


unitamount= int(unitPrice)*qty

print(unitamount)


filestring= customer_name + "," + mobile_no + "," + item_ID + "," + str(qty)+ "," +str(unitamount)
f.write(filestring)
f.close()

