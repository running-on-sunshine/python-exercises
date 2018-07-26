#  ======================================================================= #
#                            Dictionary Exercises                          #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                                Exercise 1                                #
#  ======================================================================= #

# Given the following dictionary, representing a mapping from names to 
# phone numbers:

phonebook_dict = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

# Write code to do the following:
# 1. Print Elizabeth's phone number. 
# 2. Add an entry to the dictionary: Kareem's number is 938-489-1234.
# 3. Delete Alice's phone entry.
# 4. Change Bob's phone number to '968-345-2345'.
# 5. Print all the phone entries.


# ----------------------------------- # 
# 1. Print Elizabeth's phone number.  #
# ----------------------------------- #

print phonebook_dict['Elizabeth']

# ------------------------------------------------------------------- #
# 2. Add an entry to the dictionary: Kareem's number is 938-489-1234. #
# ------------------------------------------------------------------- #

phonebook_dict['Kareem'] = '938-489-1234'

print phonebook_dict

# ------------------------------ #
# 3. Delete Alice's phone entry. #
# ------------------------------ #

del phonebook_dict['Alice']

print phonebook_dict

# ----------------------------------------------- #
# 4. Change Bob's phone number to '968-345-2345'. #
# ----------------------------------------------- #

phonebook_dict['Bob'] = '968-345-2345'

print phonebook_dict

# ------------------------------- #
# 5. Print all the phone entries. #
# ------------------------------- #

print phonebook_dict

#  ======================================================================= #
#                       Exercise 2: Nested Dictionaries                    #
#  ======================================================================= #

ramit = {
  'name': 'Ramit',
  'email': 'ramit@gmail.com',
  'interests': ['movies', 'tennis'],
  'friends': [
    {
      'name': 'Jasmine',
      'email': 'jasmine@yahoo.com',
      'interests': ['photography', 'tennis']
    },
    {
      'name': 'Jan',
      'email': 'jan@hotmail.com',
      'interests': ['movies', 'tv']
    }
  ]
}

# 1. Write a python expression that gets the email address of Ramit.
# 2. Write a python expression that gets the first of Ramit's interests.
# 3. Write a python expression that gets the email address of Jasmine.
# 4. Write a python expression that gets the second of Jan's two interests.

# ------------------------------------------------------------------ #
# 1. Write a python expression that gets the email address of Ramit. #
# ------------------------------------------------------------------ #

ramits_email = ramit['email']

print ramits_email

# ---------------------------------------------------------------------- #
# 2. Write a python expression that gets the first of Ramit's interests. #
# ---------------------------------------------------------------------- #

ramits_first_interest = ramit['interests'][0]

print ramits_first_interest

# -------------------------------------------------------------------- #
# 3. Write a python expression that gets the email address of Jasmine. #
# -------------------------------------------------------------------- #

jasmines_email = ramit['friends'][0]['email']

print jasmines_email

# ------------------------------------------------------------------------- #
# 4. Write a python expression that gets the second of Jan's two interests. #
# ------------------------------------------------------------------------- #

jans_second_interest = ramit['friends'][1]['interests'][1]

print jans_second_interest

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