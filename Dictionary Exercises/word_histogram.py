#  ======================================================================= #
#                            Dictionary Exercises                          #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                                Word Summary                              #
#  ======================================================================= #

# Write a word_histogram program that asks the user for a sentence as its 
# input, and prints a dictionary containing the tally of how many times each 
# word in the alphabet was used in the text. 

# For example:

# Please enter a sentence: To be or not to be
# {'to': 2, 'be': 2, 'or': 1, 'not': 1}

# ------------------------------------------------ #
#           Uses built-in 'split' method           #
# ------------------------------------------------ #

sentence = raw_input('Please enter a sentence: ')
dictionary = {}
space = ' '
words = sentence.split(' ')

for word in words:
    if word not in dictionary:
        dictionary[word] = 1
    else:
        dictionary[word] += 1
        
print dictionary

# ------------------------------------------------ #
#           Without built-in 'split' method        #
# ------------------------------------------------ #

sentence = 'to be or not to be'

padded_sentence = sentence + ' '

words = []
current_word = ''

for character in padded_sentence:
    if character == ' ':
        words.append(current_word)
        current_word = ''
    else:
        current_word += character

# words = ['to', 'be', 'or', 'not', 'to', 'be']

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print word_count