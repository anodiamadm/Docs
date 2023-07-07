myDict = {1: 'Rupa', 'myKey': 'Alexa', 3: "Ravina", 4: 365}

print("Item with key=3: ", myDict[3])
print("Item with key='myKey': ", myDict['myKey'])

print("Item with key=4 using get: ", myDict.get(4))
print("Try to fetch Item with nonexistent key: ", myDict.get(21, 'Not found by Sayan!'))

keysList = [2, 3, 99, 0, 'myKey']
valueList = ['Rupa', 'Ravina', 'Amaya', 'Siri', 300]
zipDict = dict(zip(keysList, valueList))
print("Dictionary by zipping 2 lists: ", zipDict)
print("Item with key=99: ", zipDict[99])
zipDict[29] = 'Alexa'
print("Dictionary after adding new element: ", zipDict)
