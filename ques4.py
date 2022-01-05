Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# Entering the marks of five students out of 100
student1_marks = float(input("Enter first student marks:"))
Enter first student marks: 92
student2_marks = float(input("Enter second student marks:"))
Enter second student marks: 95
student3_marks = float(input("Enter third student marks:"))
Enter third student marks: 98
student4_marks = float(input("Enter fourth student marks:"))
Enter fourth student marks:94
student5_marks = float(input("Enter fifth student marks:"))
Enter fifth student marks:96

# creating list of marks of these students
marks_sheet = [student1_marks, student2_marks, student3_marks, student4_marks, student5_marks]

# Printing the list in sorted manner
print("Marks of five students are:\n", sorted(marks_sheet))
Marks of five students are:
 [92.0, 94.0, 95.0, 96.0, 98.0]
