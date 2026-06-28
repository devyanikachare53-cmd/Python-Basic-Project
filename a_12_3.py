
# # Q3. (Lists + Functions + Exception Handling)
# # Create a function manage_marks() that:
# # Takes 5 subject marks as input from the user.
# # Stores them in a list.
# # Handles ValueError if non-numeric input is given.
# # Calculates and prints the average, highest, and lowest marks.
# # Sorts the list in descending order and prints it.


def manage_marks():
    # create empty list
    marks = []

    # handle try except block if any error occured 
    try: 
        for i in range(5):
            mark = int(input("Enter marks of 5 subject :"))
            marks.append(mark)
        print("Marks list",marks)

        # value-error for if any other value entered by user than value error occured
    except ValueError:
        print("Invalid Value ! Please enter valid value ")

    # total calculate for average using sum function
    total = sum(marks)
    avg = total / 5
    
    # print avg marks on output
    print("Average marks =",avg)
    
    # print highest marks of the student 
    print("Highest Subject marks in the list :",max(marks))
    
    # lowest marks of the student 
    print("Lowest Subject marks in the list :",min(marks))

    # sort list in desecding order using sort function 
    marks.sort(reverse =True)
    print("Sorted list in desending order :",marks)

# call the function
manage_marks()

