# Assignment 1


# Ques 1

# taking input from user
first_number = float(input("Enter first number:"))
second_number = float(input("Enter second number:"))
third_number = float(input("Enter third number:"))
# average of three numbers
average = ((first_number + second_number + third_number)/3)
# printing the average
print("The average of three numbers :", average)



# Ques 2

# Given constants
tax_rate = 0.20
# Each amount is in $
standard_deduction = 10000
deduction_for_dependents = 3000

# taking input from user
gross_income = float(input("Enter your income:"))
number_of_dependents = int(input("Enter the number of dependents:"))

# finding out the taxable income
taxable_income = gross_income  - standard_deduction - (deduction_for_dependents * number_of_dependents)

# finding out the income tax
income_tax = taxable_income * tax_rate
print("Your income tax is: $",income_tax)




# Ques 3

print("Student= [SID, Name, Gender, Course Name, CGPA]")
# creating the list
student = [21105035, 'KETAN', 'M', 'ECE', 9.8]
print("Student=", student)




# Ques 4

print("Marks of five students")
marks = [92, 95, 98, 94, 96]
print("List before sorting:", marks)
# Sorting the list
marks.sort()
print("List after sorting:", marks)




# Ques 5(a)

# Given list
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Removing the fourth element and printing
color.remove(color[3])
print(color)


# Ques 5(b)

# Given list
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Adding purple in place of black and pink and printing
color[3:5] = ["Purple"]
print(color)
