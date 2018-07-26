#  ======================================================================= #
#                          Exercises - Python 102                          #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                               HELLO, YOU!                                #
#  ======================================================================= #

# Same as the first exercise, but this time print the user's name in ALL CAPS,
# and also tell them the number of letters in their name

name = raw_input('WHAT IS YOUR NAME? ')
name_length = str(len(name))
hello_message = ('Hello, %s!' % name).upper()
length_message = 'YOUR NAME HAS ' + name_length + ' LETTERS IN IT! AWESOME!'

print hello_message
print length_message