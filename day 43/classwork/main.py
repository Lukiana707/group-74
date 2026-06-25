# Create a dictionary that contains a student’s name, age, and score. Then print only the score.

container = {
    "firstname": "Michael",
    "age": "15",
    "score": "B"
}

print(container["score"])


# Create a dictionary about a car and add a new value called "color".

car = {
    "model": "tesla",
    "country": "America",
    "year": 2008
}

car["color"] = "red"

print(car)



# Create a dictionary and change one of its values.

dictionary = {
    "color1": "red",
    "color2": "yellow",
    "color3": "oranege",
    "color4": "green",
}


dictionary["color4"] = "green"
dictionary["color5"] = "blue"

print(dictionary)



# Create a dictionary with 3 fruits, assign their colors, and use a for loop to print all keys and values.

fruit = {
    "orange": "orange",
    "strawberry": "red",
    "banana": "yellow"
}


for i in fruit:
    print(fruit[i], i)
    



# In the dictionary below, add another product (a nested dictionary inside the main dictionary) called "headphones",
#  which should have the following values: price → 400 / stock → 12 / rating → 4.8
store = {
    "laptop": {
        "price": 3200,
        "stock": 5,
        "rating": 4.7
    },
    "phone": {
        "price": 1800,
        "stock": 8,
        "rating": 4.5
    },
    "tablet": {
        "price": 1200,
        "stock": 3,
        "rating": 4.2
    },
    "headphones": {
        "price": 400,
        "stock": 12,
        "rating": 4.8
    }
}


# Increase the price of all products in the existing dictionary by 10% (* 1.1)
# Using the existing dictionary, create a new dictionary called high_rated that stores only products with a rating greater than 4.5