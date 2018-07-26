#  ======================================================================= #
#                             List Exercises                               #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                                   De-dup                                 #
#  ======================================================================= #

# Given a list of numbers or strings, create a new list containing the same
# elements as the first list, except with any duplicate values removed. 
# Print the list.

# numbers_list = [4, 5, -2, -3, 11, 1, 8, 3, -2, 4, 8, 1]
# de_duped_list = []

# for number in numbers_list:
#     if number not in de_duped_list:
#         de_duped_list.append(number)

# print de_duped_list

# de_duped_list = []

# ----------------------------------------------------------------- #
#                     Turn this into a function                     #
# ----------------------------------------------------------------- #

def remove_duplicates(list):
    de_duped_list = []
    for number in list:
        if number not in de_duped_list:
            de_duped_list.append(number)
    return de_duped_list

numbers = [4, 5, -2, -3, 11, 1, 8, 3, -2, 4, 8, 1]

result = remove_duplicates(numbers)

print result
