tups = (4, 45, 65, 78, 98, 8, 230)
print(tups[2:5])

print("len(tups): ", len(tups))

mySet = {4, 45, 65, 45, 78, 98, 8, 230}
print("mySet: ", mySet)

mySet.add(28)
print("Added 28: ", mySet)

mySet.remove(28)
print("Removed 28: ", mySet)

mySet.update({34, 7, 101})
print("Updated mySet: ", mySet)

mySet.clear()
print("Cleared mySet: ", mySet)