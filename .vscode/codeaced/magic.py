import random


name= str(input("Please enter your name : "))
ques= str(input("Please ask anything from 8 magic ball? :"))
ans= ""

randnum = random.randint(1,5)

if randnum== 1:
  ans = "Yes, hopefully"
elif randnum== 2:
  ans = "Maybe!"

elif randnum== 3:
  ans = "Not confirmed.."
elif randnum== 4:
  ans = "I guess no"
elif randnum== 5:
  ans = "Definetly not."
else:
  ans = "Error in backend...."

print(name, "asked" , ques)
print("8 magic ball's answer is- ", ans) 