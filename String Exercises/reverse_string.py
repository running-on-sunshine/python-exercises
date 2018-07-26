#  ======================================================================= #
#                             String Exercises                             #
#  ======================================================================= #

# Begin here:

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