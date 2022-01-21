# Assignment 2


# Program 1

input_string = "Python is a case sensitive language"

print("The length of your string is:",len(input_string))                                                                               # Finding the length of the string
print("The string after reversing:", input_string[::-1])                                                                               # reversing the string
new_string = input_string[10:26]                                                                                                       # Creating a new string
print("The string after replacing 'a case sensitive':", input_string.replace("a case sensitive", "object oriented"))                   # Replacing "a case sensitive" with "object oriented"
print("The index of substring 'a' in given input string:", input_string.find("a"))                                                     # finding the index of "a"
print("input string after removing white spaces:", input_string.replace(" ", ""))                                                      # Removing white spaces 
      


# Program 2

# Entering the details
name = "Ketan"
SID = 21105035
department_name = "ECE"
CGPA = 10

# Printing the output
print("Hey, %s Here!\nMy SID is %d\nI am from %s department and my CGPA is %d."%(name, SID, department_name, CGPA))




# Program 3


# Entering the given data
a = 56
b = 10

# Bitwise operators
print("a&b:", a&b)
print("a|b:", a|b)
print("a^b:", a^b)
print("Left shift both a and b with 2 bits \nFor a:", a<<2, ";For b:", b<<2)
print("Right shift a with 2 bits and b with 4 bits \nFor a:", a>>2, ";For b:", b>>4)





# Program 4

# Entering three numbers from users
first_number = float(input("Enter your first number:"))
second_number = float(input("Enter your sedcond number:"))
third_number = float(input("Enter your third number:"))

# Finding out the greatest number
if (first_number >= second_number) and (first_number > third_number):
    if first_number > second_number:
        print("The greatest number is the first number:", first_number)
# If two numbers are equal
    else:
        print("The greatest numbers are first number and second number:", first_number)  #Printing any one of those number

elif (second_number >= third_number) and (second_number > first_number):
    if second_number > third_number:
        print("The greatest number is second number:", second_number)
# If two numbers are equal
    else:
        print("The greatest numbers are second number and third number:", second_number)  #Printing any one of those number

elif (third_number >= first_number) and (third_number > second_number):
    if third_number > first_number:
        print("The greatest number is third number:", third_number)
# If two numbers are equal
    else:
        print("The greatest numbers are third number and first number:", third_number)    #Printing any one of those number

# If all the three numbers are equal
else:
    print("All the numbers are same")





# Program 5


# Entering the string
users_string = input("Enter the string:")

given_string = "name"

if given_string in users_string:
    print("Yes")

else:
    print("No")




# Program 6


# Entering the sides from user
side1 = int(input("Enter the first side:"))
side2 = int(input("Enter the second side:"))
side3 = int(input("Enter the third side:"))
    
# These sides will form a triangle
if (side1 < side2 +side3) and (side2 < side1 +side3) and (side3 < side2 +side1):
    print("Yes")

else:
    print("No")
