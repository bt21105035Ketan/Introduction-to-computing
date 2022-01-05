Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Taking input from user
SID = int(input("Enter your SID:\n"))
Enter your SID:
21105035
name = input("Enter your name:\n")
Enter your name:
KETAN
gender = input("Enter your gender as 'M', 'F','U' (For Unknown):\n")
Enter your gender as 'M', 'F','U' (For Unknown):
M
course_name = input("Enter your course name (AERO, CIVIL, CSE, EE, ECE, MECH, PROD, META)\n")
Enter your course name (AERO, CIVIL, CSE, EE, ECE, MECH, PROD, META)
ECE
CGPA = float(input("Enter your CGPA:\n"))
Enter your CGPA:
9.8

# Creating the list
student = [SID, name, gender, course_name, CGPA]

# Printing the list
print("Student",student)
Student [21105035, 'KETAN', 'M', 'ECE', 9.8]
