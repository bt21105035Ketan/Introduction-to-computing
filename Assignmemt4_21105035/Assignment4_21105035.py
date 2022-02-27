# Assignment 4



#Ques 1
# program for tower of Hanoi
def tower_of_hanoi(num_of_discs, source, destination, junction):
    if num_of_discs == 1:
        print("Move disc 1 from source", source, "to destination", destination)

    # for number of discs greater than 1 
    else:
        tower_of_hanoi(num_of_discs - 1, source, junction, destination)
        print("Move disc", num_of_discs, "from source", source, "to destination", destination)
        tower_of_hanoi(num_of_discs - 1, junction, destination, source)


tower_of_hanoi(3, 'peg1', 'peg3', 'peg2')




# Ques 2



print("By Recursion")


def pascal_triangle(n):
    if n == 1:
        return [[1]]
    else:
        new_row = [1]
        result = pascal_triangle(n - 1)
        last_row = result[-1]
        for i in range(len(last_row) - 1):
            new_row.append(last_row[i] + last_row[i + 1])
        new_row += [1]
        result.append(new_row)
    return result


n = int(input("Number of line you want:"))
for i in pascal_triangle(n):
    print(" " * (n - len(i)), end="")
    print(i)


# By iteration
print("By using loops")

for row in range(1, n + 1):
    print(" " * (n - row), end="")

    x = 1
    for i in range(1, row + 1):
        print(x, end="  ")
        x = x*(row - i)//i
    print()





# Ques 3


def fun(num1, num2):
    print("The Quotient of given integers is:", num1 // num2)
    print("The reminder of given integers is:", num1 % num2)


n1 = int(input("Enter first integer"))
n2 = int(input("Enter second integer"))
fun(n1, n2)

# Whether callable or not
print("The object is callable:", callable(fun))

# greater than zero or not
if n1 // n2 == 0 and n1 % n2 == 0:
    print("Both the values are zero:", True)
else:
    print("Both the values are zero:", False)

# Add (4, 5, 6) to the result
set1 = (n1 // n2, n1 % n2, 4, 5, 6)
print("The required list:", set1)
for i in set1:
    if i > 4:
        print(i)

# converting into set datatype
print("in the form of set:", set(set1))

# making set immutable
set2 = frozenset(set1)
print("Immutable set :", set2)

# largest value in set
print("The largest value in the set is:", max(set2))

# hash value of max value
print('Hash value:', hash(max(set2)))





# Ques 4
class student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def __del__(self):
        print("The created object is destroyed")


# Created the object
Student1 = student("Ketan", 21105035)

print("The name of student is:", Student1.name)
print("The SID is :", Student1.roll_no)

# Deleting object
del Student1





# Ques 5
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    # updating the salary
    def update(self):
        self.salary = 70000

    def __del__(self):
        print("The Employee record deleted")


Employee1 = Employee("Mehak", 40000)
Employee2 = Employee("Ashok", 50000)
Employee3 = Employee("Viren", 60000)


# storing the updated salary of employee Mehak
Employee1.update()

# printing the updated salary of employee Mehak
print("The updated salary of Mehak is :", Employee1.salary)


# deleting the record employee Viren
del Employee3





# Ques 6


def anagram(s1):
    if s1 == "":
        return [s1]

    else:
        ans = []
        for w in anagram(s1[1:]):
            for pos in range(len(w) + 1):
                ans.append(w[:pos] + s1[0] + w[pos:])
        return ans


word1 = input("Enter the first word:")
word2 = input("Enter the word to be checked:")

if word2.lower() in anagram(word1.lower()):
    ask = input("Is the word making sense (Y/N) : ")
    if ask == 'Y':
        print("Congrats, you have passed the friendship test")

    else:
        print("Sorry, you have failed")

else:
    print("The word is not of equal length")
