#
#   list implementation
#

list1 = [12, 2, 4]
print(type(list1))

empty = list()
empty.append(12)
empty.append(34)
empty.append('l')
empty.append(list1)

for item in empty:
    print(item)

l3 = list("ciao")
print(l3)


l4 = list([1, 2, 3])
print(l4)

print(len(empty))

print(l3.index("a"))

# position : 0 - value : z
l3.insert(6, "z")   # non va out of bound poichè non c'è bisongo degli indici, aggiunge un elemento.
print(l3)
# alla fine però normalizza l'indice
print(l3.index("z"))

l3.pop()
print(l3)