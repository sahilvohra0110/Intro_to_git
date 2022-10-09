StringInput = str(input("Please enter your word :"))
 
ReverseS = ""


for i in StringInput:
    ReverseS = i + ReverseS
 
if (StringInput == ReverseS):
    print("It is palidrome")
else:
    print("It isn't palidrome")