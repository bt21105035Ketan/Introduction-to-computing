# Assignment 3


# Ques 1

str = input("Enter your string:")
lst = str.split()           # creating a list
dict = {}                   # creating a dictionary

if len(lst) > 1:            # for multiple words in the string
    for i in lst:
        if i.lower() in dict:
            dict[i.lower()] += 1
        else:
            dict[i.lower()] = 1
else:
    for i in str.strip():               # for single word in the string
        if i.lower() in dict:
            dict[i.lower()] += 1
        else:
            dict[i.lower()] = 1

for j in dict:
    print(j, ":", dict[j])




# Ques 2


# Code for year to be leap year
def leap(year1):
    if ((year1 % 4 == 0) and (year1 % 100 != 0)) or ((year1 % 100 == 0) and (year1 % 400 == 0)):
        return leap

# For any random date or month except the last date of month
def pattern(days, months, years):
    new_days = days + 1
    new_months = months
    new_years = years

    print("DD/MM/YYYY: %d/%d/%d" % (new_days, new_months, new_years))

for i in range(1):
    year = int(input("Enter the year:"))
    month = int(input("Enter the month number(1-12):"))
    if month < 1 or month > 12:
        print("Enter the valid month number!")
        break
    else:
        day = int(input("Enter the date:"))
        # If month is of 31 days
        if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (
                month == 12):
            if day < 1 or day > 31:
                print("Enter the valid day!")
                break
            elif (day == 31) and (
                    (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10)):
                new_day = 1
                new_month = month + 1
                new_year = year
                print("DD/MM/YYYY: %d/%d/%d" % (new_day, new_month, new_year))

            # If month is December
            elif (day == 31) and (month == 12):
                new_day = 1
                new_month = 1
                new_year = year + 1
                print("DD/MM/YYYY: %d/%d/%d" % (new_day, new_month, new_year))
            else:
                pattern(day, month, year)

        # If month is of 30 days
        elif (month == 4) or (month == 6) or (month == 9) or (month == 11):

            if day < 1 or day > 30:
                print("This day is not in this month!")
                break
            elif day == 30:
                new_day = 1
                new_month = month + 1
                new_year = year
                print("DD/MM/YYYY: %d/%d/%d" % (new_day, new_month, new_year))
            else:
                pattern(day, month, year)

        # If month is february
        elif month == 2:
            if leap(year) == leap:  # If it's a leap year
                if day < 1 or day > 29:
                    print("Enter the valid day!")
                    break

                else:
                    if (day == 29) and (month == 2):
                        new_day = 1
                        new_month = month + 1
                        new_year = year

                        print("DD/MM/YYYY: %d/%d/%d" % (new_day, new_month, new_year))
                    else:
                        pattern(day, month, year)

            elif leap(year) != leap:
                if day < 1 or day > 28:
                    print("Enter the valid day!")
                    break
                else:
                    if (day == 28) and (month == 2):
                        new_day = 1
                        new_month = month + 1
                        new_year = year
                        print("DD/MM/YYYY: %d/%d/%d" % (new_day, new_month, new_year))
                    else:
                        pattern(day, month, year)



# Ques 3


number_of_elements = int(input("Enter the number of elements you want in list"))
lst = []
for idx in range(number_of_elements):
    number = int(input("Enter the number"))
    lst.append(number)
output = []
for num in lst:
    square_number = (num, num ** 2)
    output.append(square_number)
print("Your output is:", output)



# Ques 4


# function for the various grade points
def points(grade_points):
    if grade_points == 10:
        print("Your grade is 'A+' and Outstanding performance.")
    elif grade_points == 9:
        print("Your grade is 'A' and Excellent performance.")
    elif grade_points == 8:
        print("Your grade is 'B+' and Very Good performance.")
    elif grade_points == 7:
        print("Your grade is 'B' and Good performance.")
    elif grade_points == 6:
        print("Your grade is 'C+' and Average performance.")
    elif grade_points == 5:
        print("Your grade is 'C' and Below Average performance.")
    elif grade_points == 4:
        print("Your grade is 'D' and Poor performance.")
    else:
        print("Error! Write the correct grade point.")


grade_point = int(input("Enter the Grade Point:"))

points(grade_point)



# Ques 5

inp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
for row_number in range(1, 12):
    if row_number < 7:
        for spaces in range(row_number - 1):
            print(" ", end="")
        for pattern in range(0, 13 - 2 * row_number):
            print(inp[pattern], end="")
        print()
    else:
        break


# Ques 6


dict = {}
while True:
    name = input("Enter the name: ")
    SID = int(input("Enter the eight digit SID: "))
    dict[SID] = name
    more = input("Would you like to enter more details? Y/N : ")
    if more == "Y":
        continue
    else:
        break
# part a
print()
print("part(a)")
for keys in dict:
    print(keys, "is", dict[keys])

# part b
print()
print("part(b)")
dict_values = dict.values()
print("dictionary sorted by names:", sorted(dict_values))

# part c
print()
print("part(c)")
dict_keys = dict.keys()
print("dictionary sorted by SID:", sorted(dict_keys))

# part d
print()
print("part(d)")
SID_of_student = int(input("Enter the SID of the student whose detail you want : ", ))
if SID_of_student in dict:
    print("The student name is : ", dict[SID_of_student])
else:
    print("There is no such student")



# Ques 7


def fib(num):
    num1 = 0
    num2 = 1
    if num == 1:
        print("the fibonacci sequence and the average is:", num1)
    elif num > 1:
        lst = [num1, num2]
        for num3 in range(3, num + 1):
            num3 = num1 + num2
            num1 = num2
            num2 = num3
            lst.append(num3)
        print("The fibonacci sequence is:", lst)
        print("The average is:", sum(lst)/num)
    else:
        print("Enter any positive integer!")

nums = int(input("Enter your number:"))

fib(nums)



# Ques 8


# Given sets
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}
set4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}         # Created a new set of elements from range 1 to 10
# part a
new_set = set1.symmetric_difference(set2)
print()
print("(a) elements in set1 and set2 but not in both:", new_set)
# part b
new_set1 = new_set.symmetric_difference(set3)
print()
print("(b) elements only in any one of the three set:", new_set1)
# part c
new_set2 = ((set1.intersection(set2)).union(set2.intersection(set3))).union(set3.intersection(set1))
print()
print("(c) elements only in any one of the three set:", new_set2)
# part d
new_set3 = set4.difference(set1)
print()
print("(d) elements in the range 1 to 10 and not in set1:", new_set3)
# part e
new_set4 = ((set4.difference(set1)).difference(set2)).difference(set3)
print()
print("(e) elements in the range 1 to 10 but not in set1, set2 and set3:", new_set4)
