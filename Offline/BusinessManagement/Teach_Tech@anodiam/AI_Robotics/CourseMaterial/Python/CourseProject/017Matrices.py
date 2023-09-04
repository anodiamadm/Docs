from numpy import *

a1 = array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a1.dtype)
print(a1.ndim)
print(a1.shape)
print(a1.size)

a2 = a1.flatten()                      # MULTIDIM TO 1D CONVERSION
print("My 1D Array:", a2)
# noinspection PyArgumentList
a3 = a2.reshape(2, 2, 2)               # 1D TO 3D CONVERSION
print("My Multidim Array:", a3)
print(a3.ndim)
m = matrix(a1)  # MATRIX FUNCTION
print("My Matrix:", m)

m = matrix('1 2 3 4; 5 6 7 8')         # 2x4 MATRIX CREATION
print("My Matrix:", m)

m = matrix('1 2; 3 4; 5 6; 7 8')       # 4x2 MATRIX CREATION
print("My Matrix:", m)

m = matrix('1 2 3; 4 5 6; 7 8 9')      # 3x3 MATRIX CREATION
print(diagonal(m))                     # PRINTING DIAGONAL ELEMENTS
print(m.min())                         # MIN VALUE OF MATRIX
print(m.max())                         # MAX VALUE OF MATRIX

m1 = matrix('1 2 3; 4 5 6')            # 2x3 MATRIX
m2 = matrix('7 8; 9 10; 11 12')        # 3x2 MATRIX
m3 = m1 * m2
print("My Resultant Matrix:", m3)
