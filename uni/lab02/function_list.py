#
# iteration over a list.
#

list = [12, 44, 47, 90, 20]

def find(toIterate, key):
    for value in toIterate:
        if value == key:
            return value
    return False

print(find(list, 12))