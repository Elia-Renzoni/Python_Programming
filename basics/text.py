# Introduction
# @author
# @brief text in Python

# string
simple_words = "Hello World!"
# string
simple_words2 = 'Hello World!'
# multiple lines string
multiple_lines = '''\
    Ciao Mondo !
    Messaggio scritto da Elia Renzoni
'''

print(simple_words + simple_words2)
print('\n' + multiple_lines)

# repeat strings 3 times
n_repeat = 3 * 'sus'
print(n_repeat)

# array string
word = "Lorem Ipsum"
print(word[0])  # print L
print(word[2])  # print r

# slice of string
word2 = "I just learned Python"
print(word2[:]) # print all the string
print(word2[:1])    # print I
print(word2[3:5]) # print us
