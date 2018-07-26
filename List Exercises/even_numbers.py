#  ======================================================================= #
#                             List Exercises                               #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                               Even Numbers                               #
#  ======================================================================= #

# Given a list of numbers, print each number in the list that is even.

numbers_list = [4, 5, 11, 1, 8, 3]

for number in numbers_list:
    if number % 2 == 0:
        print number

# ----------------------------------------------------------------- #
#                     Turn this into a function                     #
# ----------------------------------------------------------------- #

# Turn this into a function: take one argument (list of numbers) and 
# return a new list with just the even numbers.

def print_even_num(list):
    even_numbers = []
    for number in list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
            
numbers = [4, 5, 11, 1, 8, 3]

result = print_even_num(numbers)

print result