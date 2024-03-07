numWhol = 5
numFrac = 2.5
numCplx = complex(numWhol, numFrac)
print("Type of numWhol: ", type(numWhol))
print("Type of numFrac: ", type(numFrac))
print("numCplx: ", numCplx)
print("Type of numCplx: ", type(numCplx))

intgrVal = int(numFrac)
print("Integer Value of numFrac: ", intgrVal)

fltVal = float(numWhol)
print("Float Value of numWhol: ", fltVal)

boolVal = numWhol < numFrac
print("Value of boolVal: ", boolVal)
print("int value of boolVal: ", int(boolVal))

# Range
rng = range(10)
print("Range: ", list(rng))

evnRng = list(range(6,20,2))
print("Even Numbers Range from 6-20: ", list(evnRng))
