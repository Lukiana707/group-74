#  2) ახსენით თუ რა არის ფუნქცია და როგორ შევქმნათ custom ფუნქცია
# 


# 3) შექმენით ფუნქცია რომელსაც გადაეცემა ლისთი პარამეტრად და დაითვლის ლისთში ლუწი რიცხვების რაოდენობას

def greet(num):
    for i in num:
        if i % 2 == 0:
            return i
        
print(greet([1 , 7 , 3 , 4 , 5 , 6]))

# 4) შექმენით ფუნქცია რომელსაც პარამეტრად გადაეცემა სახელი და გვარი, თქვენი დავალებაა რომ დააბრუნოთ მისალმება "Hello სახელი გვარი"

def hello_name(first_name , last_name):
    return f"my name is {first_name}, and my lastname is {last_name}"
print(hello_name("Lukiana","Mamniashvili"))



# 5) შექმენით ფუნქცია რომელიც გაარკვევს, არის თუ არა ფუნქციაში პარამეტრად გადაცემული რიცხვი ლუწი

def greet2 (num):
    if num % 2 == 0:
        return 'number is even'
    else:
        return "number is odd"

print (greet2(5)) 


# 7) კარგად ივარჯიშეთ ფუნქციებზე ლომებო <3 შემდეგ გაკვეთილზე codewars გადავალთ