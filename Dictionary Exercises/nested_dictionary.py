#  ======================================================================= #
#                            Dictionary Exercises                          #
#  ======================================================================= #

# Begin here:

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