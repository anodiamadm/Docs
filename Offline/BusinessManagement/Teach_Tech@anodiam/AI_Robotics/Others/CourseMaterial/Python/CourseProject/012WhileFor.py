# PRINTING A STRING MULTIPLE TIMES USING WHILE LOOP

i = 1
while i <= 10:
    print("Rupa")
    i = i + 1             # INCREMENT

j = 10
while j >= 1:
    print("Rupa")
    j = j - 1             # DECREMENT

# NESTED WHILE LOOP

i = 1
while i <= 10:
    print("Rupa", end="")
    j = 1
    while j <= 1:
        print(" Learns", end="")
        j = j + 1

    i = i + 1
    print()

# FOR LOOP

x = ['Rupa', 3.7, 45, 100098]
for i in x:
    print(i)
for i in ['Rupa', 3.7, 45, 100098]:
    print()
for i in range(0, 10, 3):
    print(i)

for i in range(3, 45):
    if i % 3 == 0:
        print(i)

# FOR ELSE LOOP AND FINDING PRIME NUMBER

n = 13
for i in range(2, n):
    if n % i == 0:
        print("Not Prime")
else:
    print("Prime")
