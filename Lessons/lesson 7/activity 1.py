# LESSON 7 ACTIVITY 1

# ACTIVITY 1: STUDENT CAN TAKE EXAM UNDER TWO CONDITIONS:

# Take the required input for attendance

# - Student should have attendance >= 75%

# - Check if attendance matches above criteria - Then Print "Allowed"

# - If attendance is low, Student should have a medical certificate

# - Take input for medical certificate

# - Check if student replied Yes or No

# - If Yes, Print "Allowed"

# - Else No, Print "Not Allowed"

attendance = int(input("Enter students attendance :"))

if attendance >= 75:
    print("Allowed")

else:
    cirtificate = input(" Do you have a medical cirtificate? ").lower()

    if cirtificate == "yes":
        print("Allowed")
    else:
        print(" Not Allowed")


