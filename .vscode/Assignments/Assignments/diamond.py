diamond= int(input("Please enter the diamond size"))
# running loop till user input:
for i in range(diamond):
    print(' '*(diamond-i-1)+'* '*(i+1))#printing space by diamond range into -n times and in opposite, printing star in n times 
for i in range(diamond-1):
    print(' '*(i+1)+'* '*(diamond-i-1))#decreaasing the value of stars and increasing the value of spaces
















# testnotes to understand the area utilization of o and *:
# s= 5

# for i in range(s):
#     print('o'*(s-i-1)+'* '*(i+1))

# s= 5

# for i in range(s):
#     print('* '*(i+1))
