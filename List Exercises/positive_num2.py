#  ======================================================================= #
#                             List Exercises                               #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                             Positive Numbers II                          #
#  ======================================================================= #

# Given a list of numbers, create a new list which contains every number in
# the given list which is positive.

numbers_list = [4, 5, -2, -3, 11, 1, 8, 3]
positive_numbers = []

for number in numbers_list:
    if number > 0:
        positive_numbers.append(number)
    
print positive_numbers

# ----------------------------------------------------------------- #
#                     Turn this into a function                     #
# ----------------------------------------------------------------- #

# Turn this into a function, similar to the prior exercises.

def print_positive_num(list):
    positive_numbers = []
    for number in list:
        if number > 0:
            positive_numbers.append(number)

    return positive_numbers
            
numbers = [4, 5, -2, -3, 11, 1, 8, 3]

result = print_positive_num(numbers)

print result