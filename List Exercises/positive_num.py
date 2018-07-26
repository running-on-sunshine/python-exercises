#  ======================================================================= #
#                             List Exercises                               #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                              Positive Numbers                            #
#  ======================================================================= #

# Given a list of numbers, print each number in the list that is greater 
# than zero.

# numbers_list = [4, 5, -2, -3, 11, 1, 8, 3]

# for number in numbers_list:
#     if number > 0:
#       print number

# ----------------------------------------------------------------- #
#                     Turn this into a function                     #
# ----------------------------------------------------------------- #

# Turn this into a function: take one argument (list of numbers) and
# return a new list with just the numbers greater than zero.

def print_positive_num(list):
    for number in list:
        if number > 0:
            print number
            
numbers = [4, 5, -2, -3, 11, 1, 8, 3]

print_positive_num(numbers)