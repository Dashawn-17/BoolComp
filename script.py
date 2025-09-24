# age = int(input("Enter your age: "))
#
# # = : assigment operator. it assigns values to variables. like age = 16
# # == equality operator. it gives us true if the left is equal to the right
# # age = 16
# # age == 16 return True
# # age == 17 return False
#
# if age == 16:
#     print("You are 16 years old") # if block
# else:
#     print("You are not 16 years old") # else block
#
# if age == 17:
#     print("You are 17 years old")
#     print("Congratulations!")
#
# favorite_color = input("Enter your favorite color: ")
#
# if favorite_color == "red":
#     print("Red is your favorite color")
# else:
#     print("Red is not your favorite color")
#
# # comparison operators
# # == : equality operator.
# # != not equal
# # >  greater than,  < less than
# # >=  greater than or equal to
# # <=  less than or equal to
#
#
# if favorite_color != "red":
#     print("Red is not your favorite color")
# else:
#     print("Red is your favorite color")
#
# age = int(input("Enter your age: "))
#
# if age >= 18:
#     print("Your old enough to vote")
# else:
#     print("You are not old enough to vote")
#
# # Comparison operators take two things and return True or False (boolean)
# # Logical operators.  take two booleans and return a True False (boolean)



# SELF-GUIDED COMPONENT (20 minutes - Independent work)

print("CHALLENGE 1: GRADE CALCULATOR")
print("-" * 40)
print("Create a program that determines letter grades based on a numerical score.")
print("Grading Scale:")
print("  A: 90 or above")
print("  B: 80-89")
print("  C: 70-79")
print("  F: below 70")
print()

grade = 90

if grade >= 90:
    print("Your grade is A")
else:
    if grade >= 80:
        print("Your grade is B")
    else:
     if grade >= 70:
        print("Your grade is C")
     else:
         print("You got an F")

