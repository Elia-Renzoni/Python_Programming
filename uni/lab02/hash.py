#
#
# hash maps in Python
#

myMap = dict()

def addInMap(hashMap, key, value):
    if key in hashMap.keys():
        return False
    hashMap[key] = value
    return True

def delteInMap(hashMap, key):
    if hashMap.has_key(key):
        return False
    del hashMap[key]
    return True

print(addInMap(myMap, 12, "Pippo"))
print(addInMap(myMap, 40, "Pluto"))

