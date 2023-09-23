
f = open("MyTextFile", "r")                  # r = READ

print(f)                                     # INFO ON FILE

#print(f.read())                              # READING THE FILE

#print(f.readline(), end="")                  # end DELETES SPACES
#print(f.readline())

#print(f.readline(4))                         # PRINTS DEFINED NUMBER OF CHARACTERS


f1 = open("abc", "w")                        # CREATES NEW FILE IF NO FILE NAMED "abc"

f1.write("Shine Bright Like a Diamond")      # WRITES IN YOUR NEW FILE

f1 = open("abc", "a")                        # TO APPEND/ADD MORE LINES

f1.write(" by Rihanna. ")

for data in f:                               # WRITES ALL DATA FROM ONE FILE TO ANOTHER
    f1.write(data)



# WORKING WITH IMAGE

Image= open("Duck_.jpg", "rb")                # BINARY READ (BECAUSE IMAGE)

for i in Image:                               # READING THE IMAGE
    print(i)


MyDuck = open("MyDuck_.jpg", "wb")             # BINARY WRITE (COPY IMAGE)

for i in Image:                             # COPYING THE IMAGE TO NEW FILE
    MyDuck.write(i)
