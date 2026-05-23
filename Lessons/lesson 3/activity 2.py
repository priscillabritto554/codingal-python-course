# 1) Create variables to store different types of values:
age = 16
weight= 50.2
# - `age` as a whole number (integer)

# - `weight` as a decimal number (float)

# 2) Print each variable’s value.

# 3) Print the datatype of each variable using `type()`.

# 4) Show a message that type casting will happen next.

# 5) Convert `age` from an integer to a string and store it back in `age`.

# 6) Print `age` and print its datatype again to confirm it changed.

# 7) Convert `weight` from a float to an integer and store it back in `weight`.

# 8) Print `weight` and print its datatype again to confirm it changed.
print("type of age=", type(age))
print("type of weight=",type(weight))
age = str(age)
print(age, type(age))

weight = int(weight)
print(weight, type(weight))