sum= 0

evenno= int(input("Please enter the limit of even number : "))


# running loop till given user input with 2 skipped steps.

for i in range(0, evenno+2,2):
    print(i)
    sum= sum + i

print(sum)
20