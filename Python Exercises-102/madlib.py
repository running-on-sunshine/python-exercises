#  ======================================================================= #
#                          Exercises - Python 102                          #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                                  Madlib                                  #
#  ======================================================================= #

# Prompt the user for the missing words to a Madlib sentence using the
# raw_input function.
# Side note: Added new line '\n' based on individual style preference.

greeting = 'Hello! Let\'s play some Mad Libs!\n'
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

# ----------------------------------------------------------------- #
#                     Turn this into a function                     #
# ----------------------------------------------------------------- #

name = raw_input('What is name? ')
subject = raw_input('What is subject? ')

def get_responses(name, subject):
    responses = []
    responses.append(name)
    responses.append(subject)
    
    return responses

def build_madlibs(responses):
    message = '%s\'s favorite subject in school is %s.' % (responses[0], responses[1])

    return message

responses = get_responses(name, subject)

print build_madlibs(responses)