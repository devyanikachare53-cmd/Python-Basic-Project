def grade(percentage):
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


dic = {}
while True:
    print("=========STUDENT MANGNMENT SYSTEM=========\n")
    print("1. Add Student  ")
    print("2. View All ")
    print("3. Search Student ")
    print("4. Update Student ")
    print("5. Delete Student ")
    print("6. Exit ")

    choice = int(input("Enter your Choice (1 to 6) :-"))
    #Add student
    if choice == 1:
        add = int(input("How many Student informantion you want to add ? :-"))
        
        for i in range(add):
            roll_no = int(input("Enter Student Roll Number :-"))
            name = input("Enter Student Name :-")
            city = input("Enter Student City Name :- ")
            marks_1 = int(input("Enter Marks 1 (Python) :-"))
            marks_2 = int(input("Enter Marks 2 (Java) :-"))
            marks_3 = int(input("Enter Marks 3 (Cpp) :-"))
            marks_4 = int(input("Enter Marks 4 (Operating System ) :-"))
            marks_5 = int(input("Enter Marks 5 (Software Enginerring) :-"))

            total = marks_1 + marks_1 + marks_3 + marks_4 + marks_5
            percentage = total / 5 
            print("Student percentage :-",percentage,"\n")

            dic [roll_no]= {
            # "roll_no" : roll_no,
            "name" : name,
            "city" : city,
            "marks_1" : marks_1,
            "marks_2" : marks_2,
            "marks_3" : marks_3,
            "marks_4" :marks_4,
            "marks_5" :marks_5,
            "total" :total,
            "percentage" : percentage
            }

        print("*****Student Informantion Add Successfully*****")
    #view all
    elif choice == 2 :
        if dic == 0:
            print("Student Not found")
        else :
            print("*********All Student Informantion *********** ")

        for roll_no, student in dic.items():
            print("Roll Number =", roll_no)
            print("Name =", student["name"])
            print("City =", student["city"])
            print("Marks 1 =", student["marks_1"])
            print("Marks 2 =", student["marks_2"])
            print("Marks 3 =", student["marks_3"])
            print("Marks 4 =", student["marks_4"])
            print("Marks 5 =", student["marks_5"])
            print("Total =", student["total"])
            print("Percentage =", student["percentage"])
            print("Grade =", grade(student["percentage"]))
            print("---------------------")

    #Search student
    elif choice == 3:
        print("*****Search Student******\n")
        roll_no = int(input("Enter roll number: "))

        if roll_no in dic:
            student = dic[roll_no]
            print("Roll Number =", roll_no)
            print("Name =", student["name"])
            print("City =", student["city"])
            print("Marks 1 =", student["marks_1"])
            print("Marks 2 =", student["marks_2"])
            print("Marks 3 =", student["marks_3"])
            print("Marks 4 =", student["marks_4"])
            print("Marks 5 =", student["marks_5"])
            print("Total of the Marks =",student["total"])
            print("Percentage of the Student =", student["percentage"])
            print("-----------------------------\n")
        else:
            print("Student not found!")

    #update student
    elif choice == 4:
        print("*****Update Student*****\n")
        roll_no = int(input("Enter Roll Number for update ="))
        if roll_no in dic:
            new_roll = int(input("Enter new Roll number ="))
            dic[roll_no]["new_roll" ] = new_roll
            print("New Roll Number =",new_roll)
            print("-----Updated Student Roll Number-----\n")
        else:
            print("Roll Number Not Found")

    #Delete Student
    elif choice == 5:
        print("*****Delete Student*******\n")
        roll_no = int(input("Enter roll number for remove from student info :-"))
        if roll_no in dic:
            del dic[roll_no]
            print("----Delete Student Successfully----\n")
        else:
            print("Roll number not found")

    #Exit 
    elif choice == 6:
        print("---Thank You For USing Student Managment System----\n")
        print("EXIT")
        break

