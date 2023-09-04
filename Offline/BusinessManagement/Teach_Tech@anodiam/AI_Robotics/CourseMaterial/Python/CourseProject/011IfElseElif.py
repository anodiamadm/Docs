if True:          # IF STATEMENT
    print("Print value if true: ", "I'm Human")
if False:
    print("I'm Animal")

x = 78            # FINDING EVEN AND ODD
r = x % 2
if r == 0:
    print("Even")
if r == 1:
    print("Odd")

if r == 0:        # USING IF ELSE
    print("Even")
else:
    print("Odd")

if r == 0:        # NESTED IF ELSE
    print("Even")
    if x > 90:
        print("Cool")
    else:
        print("Dull")

x = 3             # IF ELIF ELSE
if x == 1:
    print("One")
elif x == 2:
    print("Two")
elif x == 3:
    print("Three")
else:
    print("Not Found")
