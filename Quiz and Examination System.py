#  Quiz and Examination System

# Function for assces Grade according to percentage
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "Fail"


# Question Bank
questions = [
    ("Python is developed by?", "James Gosling", "Guido van Rossum", "Dennis Ritchie", "Bjarne Stroustrup", "B"),
    ("Which keyword is used for loop?", "if", "while", "input", "print", "B"),
    ("Which symbol is used for comments in Python?", "//", "#", "/*", "--", "B"),
    ("Which function is used to take input?", "input()", "print()", "len()", "type()", "A"),
    ("Python is a?", "Programming Language", "Database", "Operating System", "Browser", "A")
]

# Student Details
print("===== QUIZ MANAGEMENT SYSTEM =====")

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

score = 0
wrong_answers = []

# Quiz Start
for i, q in enumerate(questions, start=1):
    print(f"\nQuestion {i}")
    print(q[0])

    print("A.", q[1])
    print("B.", q[2])
    print("C.", q[3])
    print("D.", q[4])

    answer = input("Enter Answer (A/B/C/D): ").upper()

    while answer not in ["A", "B", "C", "D"]:
        print("Invalid Choice!")
        answer = input("Enter Answer (A/B/C/D): ").upper()

    if answer == q[5]:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")
        wrong_answers.append((q[0], q[5]))

# Result Calculation
total_questions = len(questions)
percentage = (score / total_questions) * 100
grade = get_grade(percentage)

# Result Report
print("\n===== RESULT REPORT =====")
print("Student Name :", name)
print("Roll Number  :", roll_no)
print("Total Questions :", total_questions)
print("Correct Answers :", score)
print("Wrong Answers   :", total_questions - score)

# print formated output for better understand
print("Percentage      : {:.2f}%".format(percentage))
print("Grade           :", grade)

# Wrong Answers Report
if wrong_answers:
    print("\n===== WRONG ANSWERS =====")

    for question, correct in wrong_answers:
        print("Question :", question)
        print("Correct Answer :", correct)
        print()

print("===== THANK YOU =====")





