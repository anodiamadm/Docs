# ARITHMETIC OPERATORS

a = 5
b = 6
print("sum of a and b:", a + b)
x = 7
x += 5
print("sum of x and 5:", x)
x *= 3
print("x multiplied by 3:", x)

# ASSIGNMENT OPERATORS

e, f = 4, 9
print(e)
print(f)

# UNARY OPERATOR

n = 90
n = -n
print(n)

# RELATIONAL OPERATORS

print("a greater than b:", a > b)
print("n less than b:", n < b)
print("a = b:", a == b)
print("a greater or equal to b:", a >= b)
print("a lesser or equal to b:", a <= b)
print("a not equal to b:", a != b)

# LOGICAL OPERATORS

a, b = 5, 6
print("a greater than 8 AND b greater than 7:", a > 8 and b > 7)
print("a greater than 8 AND b lesser than 7:", a > 8 and b < 7)
print("a greater than 8 OR b lesser than 7:", a > 8 or b < 7)
x = 'true'
x = not x
print("reverse of x:", x)

# BITWISE OPERATORS

print("Compliment Of 15:", ~15)                                         # COMPLIMENT
print("Bitwise AND Of 15 & 16:", 15 & 16)                               # BITWISE AND
print("Bitwise OR Of 15 & 16:", 15 | 16)                                # BITWISE OR
print("XOR Of 15 & 16:", 15 ^ 16)                                       # BITWISE XOR
print("shifting one bit to left from 10:", 10 << 1)                     # LEFT SHIFT
print("shifting one bit to right from 10:", 10 >> 1)                    # RIGHT SHIFT
