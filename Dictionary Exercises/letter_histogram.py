#  ======================================================================= #
#                            Dictionary Exercises                          #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                               Letter Summary                             #
#  ======================================================================= #

# Write a letter_histogram program that asks the user for input, and prints
# a dictionary containing the tally of how many times each letter in the 
# alphabet was used in the word. 

# For example:

# Please enter a word: banana
# {'a': 3, 'b': 1, 'n': 2}

word = raw_input('Please enter a word: ')
dictionary = {}

for letter in word:
    if letter not in dictionary:
        dictionary[letter] = 1
    else:
        dictionary[letter] += 1
        
print dictionary