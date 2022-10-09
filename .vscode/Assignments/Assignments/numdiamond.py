n=int(input("Please enter the size of diamond : "))
h = n//2
l = 1

print("Your diamond pattern is ready :")


    # Outer for loop for number of lines
for i in range(1,n+1):
         # Inner for loop for printing space
    for j in range(1,h+1):
            print (" ",end=' ')
        # Inner for loop for printing number        
    count = l//2+1    
    for k in range(1,l+1):
            print (count,end=' ')
            if (k<=(l//2)):
                count -= 1
            else:
                count += 1 
    print()
    if (i <=n // 2):
            # l decreased by 1
            # h decreased by 2
            h -= 1
            l += 2
    else:
            # l increased by 1
            # h decreased by 2
            h += 1
            l -= 2 