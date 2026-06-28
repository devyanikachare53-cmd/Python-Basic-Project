# Q2. (Strings + Loops + Functions)
# Write a function analyze_string(s) that takes a string as input and:
# Prints its length using len().
# Prints the string in reverse using slicing.
# Counts and prints how many vowels (a,e,i,o,u) are in the string (case
# insensitive).
# Uses a for loop with range() to print each character with its positive and
# negative index.
# Call this function with user input and handle empty string case.


# define function analyze_string and pass parameter
def analyze_string(s):

    # count length of the string using length function
    print("Length of the string =",len(s))

    # convert string in reverse order using slicing 
    print("String in reverse order =",s[::-1])

    # count vowels in the string using for loop 
    vowel_count = 0
    vowels = "aeiou"

    for ch in s.lower():
        if ch in vowels:
            vowel_count +=1
    print("Number of Vowels in string =",vowel_count)

    # count negative and postive index     
    for i in range(len(s)):
        negative_index = -(len(s) - i)       #count negative index decrese index 
        print(s[i] , i, negative_index)

# enter string from user 
text = input("Enter a string =")

# if-else condition for check weather string present or not
# if present it called function analyze_string and run the program

if text =="":
    print("String is empty")
else:
    print(analyze_string(text))

