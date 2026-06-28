# Q2. (Strings + Loops + Functions)
# Write a function analyze_string(s) that takes a string as input and:
# Prints its length using len().
# Prints the string in reverse using slicing.
# Counts and prints how many vowels (a,e,i,o,u) are in the string (case
# insensitive).
# Uses a for loop with range() to print each character with its positive and
# negative index.
# Call this function with user input and handle empty string case.


# # define function analyze_string and pass parameter
# def analyze_string(s):

#     # count length of the string using length function
#     print("Length of the string =",len(s))

#     # convert string in reverse order using slicing 
#     print("String in reverse order =",s[::-1])

#     # count vowels in the string using for loop 
#     vowel_count = 0
#     vowels = "aeiou"

#     for ch in s.lower():
#         if ch in vowels:
#             vowel_count +=1
#     print("Number of Vowels in string =",vowel_count)

#     # count negative and postive index     
#     for i in range(len(s)):
#         negative_index = -(len(s) - i)       #count negative index decrese index 
#         print(s[i] , i, negative_index)

# # enter string from user 
# text = input("Enter a string =")

# # if-else condition for check weather string present or not
# # if present it called function analyze_string and run the program

# if text =="":
#     print("String is empty")
# else:
#     print(analyze_string(text))


# # Q3. (Lists + Functions + Exception Handling)
# # Create a function manage_marks() that:
# # Takes 5 subject marks as input from the user.
# # Stores them in a list.
# # Handles ValueError if non-numeric input is given.
# # Calculates and prints the average, highest, and lowest marks.
# # Sorts the list in descending order and prints it.


# def manage_marks():
#     # create empty list
#     marks = []

#     # handle try except block if any error occured 
#     try: 
#         for i in range(5):
#             mark = int(input("Enter marks of 5 subject :"))
#             marks.append(mark)
#         print("Marks list",marks)

#         # value-error for if any other value entered by user than value error occured
#     except ValueError:
#         print("Invalid Value ! Please enter valid value ")

#     # total calculate for average using sum function
#     total = sum(marks)
#     avg = total / 5
    
#     # print avg marks on output
#     print("Average marks =",avg)
    
#     # print highest marks of the student 
#     print("Highest Subject marks in the list :",max(marks))
    
#     # lowest marks of the student 
#     print("Lowest Subject marks in the list :",min(marks))

#     # sort list in desecding order using sort function 
#     marks.sort(reverse =True)
#     print("Sorted list in desending order :",marks)

# # call the function
# manage_marks()


# Q4. (OOP + Lists + Exception Handling)
# Create a class Student with attributes: name, roll_no, and marks_list (a list of
# marks).
# Include methods:
# __init__ to initialize the student.
# add_mark(mark) to add a mark to the list (handle invalid marks).
# get_average() to return the average.
# display_info() to show all details.
# Create one student object, add marks using user input, and demonstrate all
# methods with exception handling.

# class student:
#     def __init__(self,name,roll_no):
#         self.name = name
#         self.roll_no = roll_no
#         self.marks_list =[]

#     def add_mark(self, mark):
#         self.marks_list.append(mark)

#     def get_average(self):
#         return sum(self.marks_list) / len(self.marks_list)

#     def info(self):
#         print("Student Name =",self.name)
#         print("Student Roll number =",self.roll_no)
#         print("Student Marks =",self.marks_list)
#         print("Average Of the Marks =",self.get_average())

# name = input("Enter Name of the student =")
# roll_no = int(input("Enter Roll Number of the Student ="))

# s = student(name,roll_no)

# for i in range(5):
#     try:
#         mark = int(input("Enter marks of 5 subject ="))
#         s.add_mark(mark)
#     except ValueError:
#         print("Invalid Value ! Please Enter Numeric Value")

# s.info()


# Q5. (Dictionaries + Functions + Control Structures)
# Write a function student_database() that uses a dictionary (roll number as key) to
# store student records.
# Provide a menu using while loop:
# 1. Add student (name, age, city)
# 2. Search student by roll number
# 3. Display all students
# 4. Exit
# Use get(), update(), and proper exception handling for invalid inputs.


# def student_database():

#     students = {}

#     while True:
#         print("\n1. Add Student")
#         print("2. Search Student")
#         print("3. Display All Students")
#         print("4. Exit")

#         try:
#             ch = int(input("Enter your choice: "))

#             if ch == 1:
#                 roll = int(input("Enter Roll No: "))
#                 name = input("Enter Name: ")
#                 age = int(input("Enter Age: "))
#                 city = input("Enter City: ")

#                 students.update({roll: {"Name": name, "Age": age, "City": city}})
#                 print("Student Added")

#             elif ch == 2:
#                 roll = int(input("Enter Roll No: "))
#                 data = students.get(roll)

#                 if data:
#                     print(data)
#                 else:
#                     print("Student Not Found")

#             elif ch == 3:
#                 for roll, data in students.items():
#                     print("Roll No:", roll)
#                     print("Name:", data["Name"])
#                     print("Age:", data["Age"])
#                     print("City:", data["City"])
#                     print()

#             elif ch == 4:
#                 print("Thank You")
#                 break

#             else:
#                 print("Invalid Choice")

#         except:
#             print("Invalid Input")

# student_database()


# Q6. (Sets + Tuples + Modules)
# Write a program that:
# Takes 10 numbers as input and stores unique numbers in a set.
# Converts that set into a tuple.
# Uses random module to pick and print 3 random numbers from the tuple.
# Uses math module to print the square root of the sum of the tuple elements.
# Handle possible exceptions.

# import random
# import math

# numbers = set()

# try:
#     for i in range(10):
#         num = int(input(f"Enter number {i+1}: "))
#         numbers.add(num)

#     t = tuple(numbers)

#     print("Set:", numbers)
#     print("Tuple:", t)

#     print("3 Random Numbers:", random.sample(t, 3))

#     total = sum(t)
#     print("Square Root of Sum:", math.sqrt(total))

# except ValueError:
#     print("Please enter numbers only!")

# except Exception :
#     print("Error:")


# # Q7. (Lambda + range() + Lists + Exception Handling)
# # Create a lambda function to calculate the square of a number.
# # Write a program that:
# # Uses range(1, 21) to generate numbers.
# # Stores the squares of these numbers in a list using the lambda function.
# # Prints only the even squares from the list.
# # Add exception handling if needed.

# # Lambda function to calculate square

# square = lambda x: x * x

# try:
#     squares = []

#     for i in range(1, 21):
#         squares.append(square(i))

#     print("All Squares:")
#     print(squares)

#     print("\nEven Squares:")
#     for num in squares:
#         if num % 2 == 0:
#             print(num)

# except Exception :
#     print("Error:")


# Q8. (Tuples + Dictionaries + OOP)
# Create a class Employee with:
# Attributes: emp_id, name, details (a tuple containing department and salary).
# Method show_details() to print all information.
# Create a dictionary where employee ID is the key and Employee object is the
# value.
# Add 3 employees and display all using a loop.

# class Employee:

#     def __init__(self, emp_id, name, department, salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.details = (department, salary)   # Tuple

#     def show_details(self):
#         print("Employee ID:", self.emp_id)
#         print("Name:", self.name)
#         print("Department:", self.details[0])
#         print("Salary:", self.details[1])
#         print()

# # Dictionary to store employees

# employees = {}

# # Add 3 employees

# for i in range(3):
    
#     emp_id = int(input("Enter Employee ID: "))
#     name = input("Enter Employee Name: ")
#     department = input("Enter Department: ")
#     salary = float(input("Enter Salary: "))

#     emp = Employee(emp_id, name, department, salary)

#     employees[emp_id] = emp


# # Display all employees

# print("\nEmployee Records:")

# for emp_id, emp in employees.items():
#     emp.show_details()


# Q9. (Strings + Sets + Exception Handling + Modules)
# Write a program that:
# Takes a sentence as input.
# Extracts all unique words (using set) from the sentence.
# Prints the unique words in sorted order.
# Uses math module to print the total number of unique words raised to power 2.
# Handle any possible exceptions gracefully.

# import math

# try:
#     # Take input
#     sentence = input("Enter a sentence: ")

#     # Convert sentence into words
#     words = sentence.split()

#     # Store unique words in a set
#     unique_words = set(words)

#     # Print unique words in sorted order
#     print("Unique words:")
#     for word in sorted(unique_words):
#         print(word)

#     # Find total unique words
#     total = len(unique_words)

#     # Print square using math module
#     print("Total unique words:", total)
#     print("Square of total unique words:", math.pow(total, 2))

# except Exception as e:
#     print("Error:", e)



# Q10. (Mini Project - Comprehensive)
# Create a Smart Calculator & Data Manager program that combines multiple
# concepts:
# Use a while loop menu with these options:
# 1. Basic Arithmetic (use functions + exception handling)
# 2. Scientific Calculations (use math module)
# 3. Generate Random Numbers (use random module)
# 4. Store Results in Dictionary (with timestamp using string)
# 5. View History (show stored results)
# 6. Exit



import math
import random

history = {}

while True:
    print("\n1. Arithmetic")
    print("2. Scientific")
    print("3. Random Number")
    print("4. Store Result")
    print("5. View History")
    print("6. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
            op = input("Enter operator (+,-,*,/): ")

            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            elif op == "/":
                result = a / b

            print("Result =", result)

        except:
            print("Invalid Input")

    elif ch == 2:
        n = int(input("Enter number: "))
        result = math.sqrt(n)
        print("Square Root =", result)

    elif ch == 3:
        result = random.randint(1, 100)
        print("Random Number =", result)

    elif ch == 4:
        time = input("Enter timestamp: ")
        history[time] = result
        print("Result Stored")

    elif ch == 5:
        print("History")
        for i in history:
            print(i, ":", history[i])

    elif ch == 6:
        print("Thank You")
        break

    else:
        print("Invalid Choice")