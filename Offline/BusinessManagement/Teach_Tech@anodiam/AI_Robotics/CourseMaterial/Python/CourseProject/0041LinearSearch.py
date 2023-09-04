
pos = -1                                         # -1 TAKEN BECAUSE INDEX COULD BE ZERO

def search(list, n):                             # CREATING SEARCH METHOD
    i = 0

    while i < len(list):
        if list[i] == n:
            globals()["pos"] = i                 # ACCESSING & MODIFYING GLOBAL VARIABLE
            return True
        i = i+1

    return False

list = [9, 2, 45, 67, 5, 10, 1]

n = 9

if search(list, n):
    print("Found at", pos)
else:
    print("Not Found")


# ALTERNATIVE WITH FOR LOOP & USER INPUT


list = [9, 2, 45, 67, 5, 10, 1]

n = int(input("Enter a Number"))                    # TAKING INPUT FROM USER

pos = -1

for i in range(len(list)):

    globals()['pos'] = i

    if list[i] == n:
        print("Found at", pos)

        break
else:
    print("Not found")
