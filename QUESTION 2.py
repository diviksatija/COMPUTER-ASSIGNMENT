#QUESTION 2
Gross_Income = int(input("Enter the Gross Income : "))
Dependent = int(input("Enter Dependent : "))
Standard_deduction = 10000
Dependent_deduction_amount = Dependent * 3000
Taxable_Income = Gross_Income - Standard_deduction - Dependent_deduction_amount
Tax = float((20/100) * (Taxable_Income))  # Tax is 20% of Taxable_Income
print("Your income tax : ", Tax)
