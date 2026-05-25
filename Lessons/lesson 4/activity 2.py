#M1 Lesson 4 Activity 2

# 1) Take the total withdrawal amount as input from the user and store it in `Amount`.

# 2) Find how many 100-rupee notes are needed:

# Divide `Amount` by 100 (whole number division) and store it in `note_1`.

# 3) Find the remaining amount after taking out 100-rupee notes:

# Use the remainder of `Amount` after dividing by 100.

# 4) From the remaining amount, find how many 50-rupee notes are needed:

# Divide the remainder by 50 (whole number division) and store it in `note_2`.

# 5) Find the remaining amount after taking out 50-rupee notes:

# Use the remainder after dividing by 50.

# 6) From the remaining amount, find how many 10-rupee notes are needed:

# Divide the remainder by 10 (whole number division) and store it in `note_3`.

# 7) Print the number of 100-rupee notes, 50-rupee notes, and 10-rupee notes.
amount = int(input("enter the amount "))

note_100 = amount // 100
amount = amount % 100
note_50 = amount // 50
amount = amount % 50
note_10 = amount //10
print("100 rupee notes = ",note_100)
print("50 rupee notes = ",note_50)
print("10 rupee notes = ",note_10)
