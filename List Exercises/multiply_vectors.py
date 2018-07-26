#  ======================================================================= #
#                             List Exercises                               #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                             Multiply Vectors                             #
#  ======================================================================= #

# Given two lists of numbers of the same length, create a new list by 
# multiplying the pairs of numbers in corresponding positions in the two lists.

# Example:

# [2, 4, 5] x [2, 3, 6] = [4, 12, 30]

numbers_one = [2, 4, 5]
numbers_two = [2, 3, 6]
multiplied_list = []

for i in range(len(numbers_one)):
    product = numbers_one[i] * numbers_two[i]
    multiplied_list.append(product)

print multiplied_list

# ----------------------------------------------------------------- #
#                     Turn this into a function                     #
# ----------------------------------------------------------------- #

# Turn the rest of these exercises into functions. Tt's up to you to 
# figure out how many arguments the function needs!

def multiply_vectors(list_one, list_two):
    multiplied_list = []
    for i in range(len(list_one)):
        product = list_one[i] * list_two[i]
        multiplied_list.append(product)
    return multiplied_list

list_one = [2, 4, 5]
list_two = [2, 3, 6]

result = multiply_vectors(list_one, list_two)

print result