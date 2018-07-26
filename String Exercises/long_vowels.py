#  ======================================================================= #
#                             String Exercises                             #
#  ======================================================================= #

# Begin here:

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