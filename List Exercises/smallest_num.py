#  ======================================================================= #
#                             List Exercises                               #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                              Smallest Number                             #
#  ======================================================================= #

# Given a list of numbers, print the smallest of the numbers.

numbers_list = [4, 5, 11, -1, 4]

smallest_num = numbers_list[0]

for number in numbers_list:
    if number < smallest_num:
        smallest_num = number

print smallest_num

# ----------------------------------------------------------------- #
#                     Turn this into a function                     #
# ----------------------------------------------------------------- #

def find_smallest_num(list):
    smallest_num = list[0]
    for number in list:
        if number < smallest_num:
            smallest_num = number

    return smallest_num

numbers = [4, 5, 11, -8, 4]

result = find_smallest_num(numbers)

print result

