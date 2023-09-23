
x = 7
y = 0                                            # NORMAL STATEMENTS

try:
    print(x/y)                                   # CRITICAL STATEMENT
except Exception:
    print("Hey, User a number is not divisible by zero")

print("Bye")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

a = 7
b = 4

try:
    print("Opened")
    print(a/b)
    n = int(input("Enter a number"))
    print(n)

except ZeroDivisionError as e:                                           # PRINTING THE ERROR MESSAGE
    print("Hey User, a number is not divisible by zero", e)

except ValueError as v:
    print("Invalid input", v)

except Exception as e:
    print("Something went wrong. . .")

finally:                                                         # EXECUTES REGARDLESS OF ERROR
    print("Closed")

print("Bye")
