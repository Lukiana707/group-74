 # Equal-to (==) checks if two values are the same.
# Not-equal (!=) checks if two values are different



print(5 == 5)        # True, because both numbers are equal
print("cat" == "dog")  # False, strings are different
print(10 == 2 * 5)   # True, because 2*5 equals 10

print(3 != 4)        # True, because 3 is not equal to 4
print("apple" != "banana")  # True, different strings
print(7 != 7)        # False, because both are equal

# Conditional statements use these keywords:
# if – თუ პირობა მართალია, კოდი შესრულდება
# elif – სხვა პირობა, თუ პირველი არ იყო მართალი
# else – ყველა სხვა შემთხვევისთვის

age = 20

if age > 18:  # თუ ასაკი მეტია 18-ზე
    print("You are an adult!")
elif age == 18:  # თუ ასაკი ზუსტად 18-ია
    print("You are 18yo!")
else:  # ყველა სხვა შემთხვევაში
    print("You are a teenager!")

age = int(input("Enter your age: "))

if age > 18:
    print("You are an adult!")
elif age == 18:
    print("You are 18yo!")
else:
    print("You are a teenager!")

i = 0
while i < 5:
    print("Lukiana")
    i += 1  # გაზრდა 1-ით ყოველი ციკლის შემდეგ


total = 0
for num in range(1, 7):  # 1-დან 6-მდე
    print(num)
    total += num  # ჯამში დამატება

print("Sum:", total)

user_name = input("Enter your name: ")
my_name = "Lukiana"

if user_name == my_name:
    print("The names are the same")
else:
    print("The names are different")