#John manages a private vehicle parking site at a hospital. The charge for a 2-wheeler vehicle is 10 and a 4-wheeler vehicle is 20. He would like to know how much money he has collected at the end of the day for n number of 2-wheelers parked and m number of 4-wheelers parked on the day.


print("Welcome to John Private Parking Pvt.Ltd. Billing application")
noOfTwoWheeler=int(input("Enter of Two Wheeler count : "))
ChargeofTwoWheeler=int(input("Enter Two wheeler parking charge : "))
noOfFourWheeler=int(input("Enter of Four Wheeler count : "))
ChargeofFourWheeler=int(input("Enter Four wheeler parking charge : "))
TotalCollection=int(noOfTwoWheeler*ChargeofTwoWheeler+noOfFourWheeler*ChargeofFourWheeler)
print("That's Great John!! Your Total Collection for is", TotalCollection,"So Far")



