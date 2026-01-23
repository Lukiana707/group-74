# Program 1: Classify age
age = int(input("Enter your age: "))

if 0 <= age <= 12:
    print("Child")
elif 13 <= age <= 19:
    print("Teenager")
elif 20 <= age <= 59:
    print("Adult")
else:
    print("Pensioner")

# Program 2: Classify number
number = float(input("Enter a number: "))

if number < 0:
    print("Negative")
elif number == 0:
    print("Zero")
elif 0 < number < 100:
    print("Small number")