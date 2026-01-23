#A nested if is an if statement placed inside another if or else block.
#It allows you to make decisions within decisions, like a flowchart that branches further depending on earlier outcomes.

# Ask for user input
age = int(input("Enter your age: "))
name = input("Enter your name: ")

# First condition: check age
if age < 18:
    print("Denied")
else:
    # Nested condition: check name
    if name == "Deme":
        print("Denied")
    else:
        print("Accepted")