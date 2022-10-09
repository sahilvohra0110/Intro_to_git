# to check the prime no list

from re import I


primenum= int(input("Please enter the last limit of even no sum : "))
sum= 0

# running loop to find out the prime number list of given limit i.e. primenum variable.

for i in range (2,primenum+1):
    for j in range(2,i):
        if (i%j == 0):
            break
    else:
        # optional, if we don't want to print all prime no against the user input, then we can remove 17th line.
        print(i)
        # now doing sum of all listed prime numbers by-
        sum= sum + (i)
print("Hence, the sum of given prime number limit is :", sum )