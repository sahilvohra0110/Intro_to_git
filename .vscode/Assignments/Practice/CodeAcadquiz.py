num=int(input("Enter the depth of the diamond : "))

def diamondpattern(num):

    for i in range(1,num+1):
        for k in range(0,num-i):
          print(" ",end="")
        for j in range((2*i)-1):
           print("*",end="")
        print()

    for i in range(num-1):
        for k in range(0,i+1):
          print(" ",end="")
        for j in range((2*num)-(2*i)-1-2):
          print("*",end="")
        print()

diamondpattern(num)

