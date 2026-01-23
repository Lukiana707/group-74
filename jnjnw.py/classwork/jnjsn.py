#1

# print()
# Outputs displays information on the screen that you put down.
# type()
# Shows the data type of a value ( int, str, float, list, etc.).
# range()
# Generates a sequence of numbers (e.g., 0–10).
# Often used in loops.
# str()
# Converts a value into a string (text).
# int()
# Converts a value into an integer (whole number).
#----------------------------------------------------------
#2

# .upper() –  converts the entire string to uppercase.

# .lower() – converts the entire string to lowercase.

# .capitalize() –capitalizes the first letter of the string and makes the rest lowercase.

# .swapcase() –  switches uppercase letters to lowercase and lowercase letters to uppercase.

# .find() – searches for a substring inside the string and returns the starting index of the first occurrence like if u input i in Anna it wont find the letter so it will input -1
#--------------------------------------------------------------------------------------------------------------------------------------------------
#3

result = 0

for i in range(0, 31, 2):
    print(i)
    result += 1

print("Number of loop repetition:",  result)


#4

#Arguments are values you give to a function so it can do something with them.

print(10)          # int
print(10.5)        # float
print("hello")     # str
print(True)        # bool

#5

lastname = "mamniashvili"

print(lastname.upper())
print(lastname.lower())
print(lastname.capitalize())
print(lastname.swapcase())
print(lastname.find("m"))

