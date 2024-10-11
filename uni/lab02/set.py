#
# sets
#

mySet = set()

def addInSet(emptySet, valueToAdd):
    emptySet.add(valueToAdd)
    print("+")

def printValues(setToPrint):
    for value in setToPrint:
        print(value)
    print("End")


for toAdd in range(12, 56, 1):
    addInSet(mySet, toAdd)

printValues(mySet)