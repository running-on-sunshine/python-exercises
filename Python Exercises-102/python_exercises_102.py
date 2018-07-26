#  ======================================================================= #
#                          Exercises - Python 102                          #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                               Hello, you!                                #
#  ======================================================================= #

# Prompt the user for their name using the raw_input function.
# Upon receiving his their, you will say hello to them. 

name = raw_input('What is your name? ')
message = 'Hello, ' + name + '!'

print message

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

#  ======================================================================= #
#                                  Madlib                                  #
#  ======================================================================= #

# Prompt the user for the missing words to a Madlib sentence using the 
# raw_input function. 

# Side note: Added new line '\n' based on individual style preference.

greeting = 'Hello! Let\'s play some Madlibs!\n'
horizontal_line = '-------------------------------\n'
styled_greeting = horizontal_line + greeting + horizontal_line

instruction = 'Please fill in the blanks below:\n'
sentence = '_____(name)____\'s favorite subject in school is ____(subject)____.\n'

print styled_greeting
print instruction
print sentence

name = raw_input('What is name? ')
subject = raw_input('What is subject? ')

returned_sentence = '\n%s\'s favorite subject in school is %s.\n' % (name, subject)

print returned_sentence