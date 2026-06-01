# ACTIVITY 3 - CUSTOMIZE YOUR FOOD DELIVERY ORDER

# 1) Display a menu asking the user to select a food category:

# - 1 for Biryani

# - 2 for Pizza

# 2) Take the user’s input and store it in `choice`.

# 3) If `choice` is 1 (Biryani):

# a) Show Biryani options (Veg / Chicken)

# b) Take the user’s input for Biryani type and store it in `choice2`

# c) If `choice2` is 1, print "Your order is on the way: Veg Biryani"

# Else, print "Your order is on the way: Chicken Biryani"

# 4) Else if `choice` is 2 (Pizza):

# a) Show pizza options (Paneer / Chicken)

# b) Take the user’s input for pizza type and store it in `choice3`

# c) If `choice3` is 1, print "Your order is on the way: Paneer Pizza"

# Else, print "Your order is on the way: Chicken Pizza"

# 5) Else (if `choice` is not 1 or 2):

# Print "Wrong choice!"

print("What would you like to order?  1- biriyani , 2- pizza")

choice = int(input("Enter your choice_ "))

if choice == 1:
    choice_1 = int(input(" Enter 1-veg , 2-chicken_ "))
    if choice_1 == 1:
        print ("Your order is on the way: veg Biryani")

    else:
        print("Your order is on the way: Chicken Biryani")

elif choice == 2:
    choice_2 = int(input(" Enter 1-paneer , 2-chicken_ "))

    if choice_2== 1:
        print ("Your order is on the way: paneer pizza")

    else:
        print("Your order is on the way: Chicken pizza")

else:
    print("Wrong choice!")



