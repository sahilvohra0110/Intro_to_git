TypeOfLoan=input("Please enter the loan type")
AmountOfLoan=int(input("Please enter the amount of loan"))
InterestRate=int(input("Please enter the interest rate per annum"))
TotalTenureInYears=int(input("Please enter total duration of loan in years"))
TotalAmountPayble=(AmountOfLoan+(AmountOfLoan*InterestRate))*TotalTenureInYears
TotalMonthlyEMI=TotalAmountPayble/(TotalTenureInYears*12)
TotalInterest=(AmountOfLoan*InterestRate)/100
print("Your Total Amount Payble is", TotalAmountPayble, )
print("Your Total Interest is", TotalInterest)
print("Your Total Monthly EMI will be", TotalMonthlyEMI)