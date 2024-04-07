# Introduction
# @author Elia Renzoni
# @brief List in Python

list_of_same_types = [12, 3, 4, 5, 6]
print(list_of_same_types)
print(list_of_same_types[2:])
print(list_of_same_types[-4])   # print 3

list_of_different_types = ["str", 12, 5.5]
print(list_of_different_types)
list_of_different_types.append("OSS")
print(list_of_different_types)

# list concatenation
first_list = [33, 55, 66]
last_list = [7, 8] + first_list
print(last_list)

# pointer reference to a list 
rgb = ['Green', 'Blue', 'Red']
rgba = rgb # pointer
# so evry change era mutual
rgba.append('Alpha')
print(rgba)
print(rgb)


# remove elements in a list
tiny_list = [12, 66, 7]
tiny_list[1] = []
print(tiny_list)

# replace elements in a list
another_tiny_list = [33, 4, 1]
another_tiny_list[:] = [2, 3, 7]
print(another_tiny_list)

# nested list
list1 = ["Ciao", "Ciaone"]
list2 = [6.8, 7, 8.9]
list3 = [list1, list2]
print(list3)