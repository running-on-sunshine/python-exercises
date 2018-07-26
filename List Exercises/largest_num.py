#  ======================================================================= #
#                             List Exercises                               #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                              Largest Number                              #
#  ======================================================================= #

# Given a list of numbers, print the largest of the numbers.

numbers_list = [-4, 5, -11, 1, -4]

largest_num = numbers_list[0]

for number in numbers_list:
    if number > largest_num:
        largest_num = number

print largest_num

# ----------------------------------------------------------------- #
#                     Turn this into a function                     #
# ----------------------------------------------------------------- #

# Turn this into a function: take one argument (a list of numbers) 
# and return the largest.

def find_largest_num(list):
    largest_num = list[0]
    for number in list:
        if number > largest_num:
            largest_num = number

    return largest_num

numbers = [-4, 5, -11, 1, -4]

result = find_largest_num(numbers)

print result