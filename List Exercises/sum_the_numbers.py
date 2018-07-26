#  ======================================================================= #
#                             List Exercises                               #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                             Sum the Numbers                              #
#  ======================================================================= #

# Given a list of numbers, print their sum. When I say given something, 
# just make something up and store it in a variable.

numbers_list = [11, 4, 5, 1, 4]
total = 0

for number in numbers_list:
    total += number

print total

# ----------------------------------------------------------------- #
#                     Turn this into a function                     #
# ----------------------------------------------------------------- #

# Next, turn this into a function! It should take in one argument 
# (a list of numbers) and return their sum!

def sum_the_numbers(numbers_list):
    total = 0
    for number in numbers_list:
        total += number

    return total

numbers = [11, 4, 5, 1, 4]

result = sum_the_numbers(numbers)

print result