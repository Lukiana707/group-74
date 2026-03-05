#  1) შექმენით join ფუნქციის კლონი თქვეი custom ფუნქციით, არ გამოიყენოთ join ფუნქცია

def join_clone(symbol, arr):
    result = ""
    
    for i in arr:
        result += f"{i}{symbol}"
    
    return result[:-1]

print(join_clone("$", ["nika", "vano", "giorgi"]))
print("$".join(["nika", "vano", "giorgi"])) 

# 2) შექმენით split ფუნქციის კლონი თქვენი custom ფუნქციით, არ გამოიყენოთ split ფუნქცია
def split_clone(str, symbol):
    result = []
    test = ""
    
    for i in str:
        if i != symbol:
            test += i
        else:
            result.append(test)
            test = ""

    result.append(test)
    return result

print(split_clone("gamarjoba rogor xar", " ")) 


# 3) შექმენით ერთი tuple რომელსაც ექნება გადაცემული სახელები, თქვენი დავალებაა რომ შექმნათ რამდენიმე ცვლადი ერთდროულად,
#  შეინახოთ ამ tuple ში მოცემული სახელები თითოეულ ცვლადში და დაპრინტოთ თითოეული სახელი

listen = ("Lukiana", "deme", "Monica")

for i in listen:
    print(i)


# 4) შექმენით ინტეჯერების tuple 8 რიცხვით, თქვენი დავალებაა რო მეხუთე პოზიციაზე მდგარი რიცხვი შეცვალოთ თქვენი ასაკის რიცხვით

numbers = (1, 2, 3, 4, 5, 6, 7, 8)

numbers[:5] = 10

print(numbers)


# 5)კომენტარის სახით ახსენით ASERISK ოპერატორის დანიშნულება

# 6)შექმენით tuple, სადაც გექნებათ 10 მნიშვნელობა და unpacking + asetrisk-ის გამოყენებით შექმენით 5 ცვლადი, პირველ ცვლადს მიანიჭეთ tuple-დან 
# პირველი მნიშვნელობა, მეორე ცვლადს მეორე მნიშვნელობა, მესამე ცვლადს დარჩენილი მნიშვნელობა გარდა ბოლო ორისა, მეოთხე ცვლადს ბოლოს წინა მნიშვნლელობა და მეხუთე ცვლადს ბოლო მნიშვნელობა

# ანუ: (item1, item2, item3, item4, item5, item6, item7, item8, item9, item19)

# v1 = უნდა ინახავდეს item1-ს

# v2 = უნდა ინახავდეს item2-ს

# v3 = უნდა ინახავდეს item1, item2, item3, item4, item5, item6, item7, item8-ს

# v4 = უნდა ინახავდეს item9-ს

# v5 = უნდა ინახავდეს item10-ს