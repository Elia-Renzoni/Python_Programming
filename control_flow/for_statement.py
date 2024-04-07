# Control flow instructions
# @author Elia Renzoni
# @brief for control flow instruction

text = input("Inserisci una stringa: ")

for word in text:
    print(word + '\n')


# iteration over a list
list = [12, 66, 5, 33, 7, 9]
for n in list:
    print(n)

# iteration over a collection
# its like a key-value store
collection = {
    "Elia": 12,
    "Giovanni": 77,
    "Mattia": 8
}

for key, value in collection.items():
    if key == "Elia":
        print(value)
    elif key == "Mattia":
        print("SIUM")

# iteration over range
# range function just create n random integer values
for n in range(128):
    print(n)

list = [12, 44, 55, 6]
for index in range(len(list)):
    if list[index] == 44:
        print(list[index])