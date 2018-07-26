#  ======================================================================= #
#                             String Exercises                             #
#  ======================================================================= #

# Begin here:

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