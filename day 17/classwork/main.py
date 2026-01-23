#We use 'elif' to avoid checking every 'if' condition unnecessarily.
#It ensures that once a condition is met, the rest are skipped, making the code more efficient and readable.



age = int(input("Please enter your age: "))

if age >= 64:
    print("elderly discount")
elif age >= 10:
    print("child discount")
else:
    print("regular price")