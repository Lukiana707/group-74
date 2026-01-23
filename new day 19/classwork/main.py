
# fruits = ["Apple", "Banana", "Orange", "Grapes"]

# print(fruits[0])
# print(fruits[-1])

# fruits + fruits + ["mango"]

# fruits[2] = "Kiwi"
# print(fruits)
# #-------------------------------------------------------
# numbers = [10,20,30,40,50,60,70]

# print(numbers[:3])

# print(numbers[-2])

# print(numbers[2:6])

# print(numbers[::2])
# #--------------------------------------------------------
# surname = "Mamniashvili"

# reversed_letters = surname[::-1]

# print(reversed_letters)
# #--------------------------------------------------------
# # slicing allows us to take a part of a list or a string 

# # list is a mutable it can  be changed 

# #--------------------------------------------------------


nums = [3, 8, 11, 24, 17, 4, 9]

odd_sum = sum(n for n in nums if n % 2 != 0)
print( odd_sum)

text = input("Enter text: ")


hi = (" ", "")

if hi == hi[::-1]:
    print("Text is Palindrome")
else:
    print("Not palindrome")






