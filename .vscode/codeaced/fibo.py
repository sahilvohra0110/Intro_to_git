

# evennumber = int(input("Please enter the range of even number"))
# sum = 0

# for i in range(0,evennumber):
#     if (i%2)==0:
#         print(i)
#         sum = sum+i
# print(sum)


# Fiboseries

# Question- 0+1=1, 1+1=2, 2+1=3, ..

fiboseries = int(input("Please enter fibo ending series"))
a = 0
b = 1
c = 0


while c<fiboseries :
    print(c)
    a= b
    b= c
    c= a+b 
