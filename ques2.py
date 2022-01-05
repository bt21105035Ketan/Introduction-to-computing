Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Given constants
tax_rate = 0.20
# Each amount is in $
standard_deduction = 10000
deduction_for_dependents = 3000

# taking input from user
gross_income = float(input("Enter your income:"))
Enter your income: 80000.00
number_of_dependents = int(input("Enter the number of dependents:"))
Enter the number of dependents: 3

# finding out the taxable income
taxable_income = gross_income  - standard_deduction - (deduction_for_dependents * number_of_dependents)

# finding out the income tax
income_tax = taxable_income * tax_rate
print("Your income tax is: $",income_tax)
Your income tax is: $ 12200.0
