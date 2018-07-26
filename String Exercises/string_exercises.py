#  ======================================================================= #
#                             String Exercises                             #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                             Uppercase a String                           #
#  ======================================================================= #

# Given a string, print the string uppercased. #string #easy

string = raw_input('Enter a message: ')
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
uppercased_string = ''

for letter in string:
    for i in range(len(lowercase)): 
        lowerletter = lowercase[i]
        if lowerletter == letter:
            letter = uppercase[i]
            break
    
    uppercased_string += letter

print uppercased_string

#  ======================================================================= #
#                             Capitalize a String                          #
#  ======================================================================= #

# Given a string, print the string capitalized. #string #easy

string = raw_input('Enter a message: ')
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
capitalized_string = ''

for i in range(len(string)):
    letter = string[i]
    if i == 0 and string[i] in lowercase:
        for j in range(len(lowercase)):
            if string[i] == lowercase[j]:
                letter = uppercase[j]
                break
    elif (string[i - 1] in lowercase) or (string[i - 1] in uppercase):
        letter = string[i]
    else:
        for j in range(len(lowercase)):
            if string[i] == lowercase[j]:
                letter = uppercase[j]
                break
                
    capitalized_string += letter 

print capitalized_string

#  ======================================================================= #
#                              Reverse a String                            #
#  ======================================================================= #

# Given a string, print the string reversed.

string = raw_input('Enter a message: ')
string_length = len(string)
string_reversed = ''

for i in range(string_length-1, -1, -1):
    string_reversed += string[i]

print string_reversed

#  ======================================================================= #
#                                 Leetspeak                                #
#  ======================================================================= #

# Given a paragraph of text as a string, print the paragraph in leetspeak. 
# To translate a string to leetspeak, you need to replace make the following 
# character replacements (treat all input characters as uppercase):

# A => 4
# E => 3
# G => 6
# I => 1
# O => 0
# S => 5
# T => 7

# Inspirado en la recuerda de mi hogar y las conchas requisimas de la panaderia 
# cerca de la casa. Ayy..las recuerdas.

# English: Inspired by my memory of home and the delicious conchas (a Mexican 
# sweet bread with a sugar topping in the design of a shell, hence the name, 
# 'concha.') from the panaderia (a bakery! mmm!) near our house. Oh...the memories. 

string = 'BUENOS DIAS! HOY TENEMOS ALGO MUY RICO! LAS CONCHAS SERVIDAS CON CAFE. MMM!'
leetspeak_string = ''

for letter in string:
    if letter == 'A':
        letter = '4'
    elif letter == 'E':
        letter = '3'
    elif letter == 'G':
        letter = '6'
    elif letter == 'I':
        letter = '1'
    elif letter == 'O':
        letter = '0'
    elif letter == 'S':
        letter = '5'
    elif letter == 'T':
        letter = '7'

    leetspeak_string += letter

print leetspeak_string

#  ======================================================================= #
#                              Long-long Vowels                            #
#  ======================================================================= #

# Given a word as a string, print the result of extending any long vowels to
# the length of 5.

#  Examples:

# Good => Goooood
# Cheese => Cheeeeese
# Man => Man
# Spoon => Spooooon

word = 'good'
long_vowel_word = ''

vowels = ['a', 'e', 'e', 'o', 'u']

for i in range(len(word)):
    letter = word[i]
    if word[i] in vowels:
        if word[i] != word[i + 1]:
            letter = word[i]
        else:
            letter = word[i] * 4
            
    long_vowel_word += letter

print long_vowel_word