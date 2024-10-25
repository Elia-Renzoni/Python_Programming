import numpy as np

a = np.array([1, 2, 3])
print(a)
print(a[1])
print(type(a))
print(type(a[1]))
print(a.dtype)

# matrix 3x3
a2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a2)
# ndim, n-dimensionalità dell'array, mono e bi.
print(a.ndim)
print(a2.ndim)
# numero di elementi in lunghezza e larghezza
# (3)
print(a.shape)
# (3, 3)
print(a2.shape)

# size
print("Size: quanti elementi sono contenuti nell'array per dimensione:")
print(a.size)
print(a2.size)

print(a2[1])
# accesso al primo elemento della dimensione in posizione 1
print(a2[1][0])

# @param, matrice da inizializzare
z = np.zeros((3, 4))
print(z)

r = np.arange(1, 10, 2)
print(r)

# reshaping
b = np.array([1,2,3,4])
print(b)
print(b.reshape((2, 2)))


# ravel
print(a2.ravel())

# stampa i singoli elementi
for e in a2.flatten():
    print(e)

print("----")

for e in a2[1]:
    print(e)

print("----")
print(a2.sum())
print("Somma per righe:")
print(a2.sum(axis=1))