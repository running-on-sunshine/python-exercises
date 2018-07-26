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