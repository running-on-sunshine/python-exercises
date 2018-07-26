#  ======================================================================= #
#                             List Exercises                               #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                             Multiply a List                              #
#  ======================================================================= #

# Given a list of numbers, and a single factor (also a number), create a 
# new list consisting of each of the numbers in the first list multiplied 
# by the factor. Print the new list out to the screen.

numbers_list = [4, 5, -2, -3, 11, 1, 8, 3]
multiplied_list = []
factor_input = raw_input('Enter a factor: ')
factor = int(factor_input)

for number in numbers_list:
    product = number * factor
    multiplied_list.append(product)

print multiplied_list

# ----------------------------------------------------------------- #
#                     Turn this into a function                     #
# ----------------------------------------------------------------- #

# Turn this into a function which takes TWO arguments and returns a new list.

def multiply_list(list, factor): 
    for number in list:
        product = number * factor
        multiplied_list.append(product)
    return multiplied_list

numbers = [4, 5, -2, -3, 11, 1, 8, 3]
multiplied_list = []

factor_input = raw_input('Enter a factor: ')
factor = int(factor_input)

result = multiply_list(numbers, factor)

print result