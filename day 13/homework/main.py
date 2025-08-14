# A while loop repeatedly executes a block of code as long as its condition remains true, and it stops when the condition becomes false.
counter = 0
while counter <= 4:
    print(counter)
    counter += 1
# -----------------
counter = 0
while counter < 3:
    print('hello')
    counter += 1
# -----------------
counter = 0
while counter < 3:
    print('hello')
    counter += 1
# ------------------
counter = 1
while counter <= 5:
    if counter == 3:
        print('average')
    counter += 1
# -------------------
counter = 1
while counter <= 5:
    if counter > 2:
        print(counter)
    counter += 1
# --------------------
counter = 0
while True:
    if counter == 4:
        break
    print(counter)
    counter += 1
# ------------------------