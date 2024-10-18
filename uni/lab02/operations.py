#
# basic I/O operations
#

userInput = input("Type something...\n")
print(f"{userInput}")

# files
file = open("foo.txt", "w")
file.write("Simple Line")
file.close()

f = open("foo.txt", "r")
s = f.read()
f.close()
print(s)

values = ["1233\t", "5555\t"]
file2 = open("bar.txt", "w")
file2.writelines(values)
f.close()

with open("bar.txt", "a") as i:
    i.write("Miao")
