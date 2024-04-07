# Control Flow Instructions
# @author Elia Renzoni
# @brief if statament

number = int(input("Inserisci un numero compreso tra 20 e 40, estremi inclusi: "))

if number >= 20 and number <= 40:
    print("OK!\n")
else:
    print("No!")

control = int(input("Inserisci un numero intero: "))

if number < 0:
    print("Numero negativo")
elif number == 0:
    print("Numero uguale a 0")
else:
    print("Numero maggiore di 0")