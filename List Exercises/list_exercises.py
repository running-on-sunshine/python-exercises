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

#  ======================================================================= #
#                               Even Numbers                               #
#  ======================================================================= #

# Given a list of numbers, print each number in the list that is even.

numbers_list = [4, 5, 11, 1, 8, 3]

for number in numbers_list:
    if number % 2 == 0:
        print number

#  ======================================================================= #
#                              Positive Numbers                            #
#  ======================================================================= #

# Given a list of numbers, print each number in the list that is greater 
# than zero.

numbers_list = [4, 5, -2, -3, 11, 1, 8, 3]

for number in numbers_list:
    if number > 0:
      print number

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

#  ======================================================================= #
#                             Multiply Vectors                             #
#  ======================================================================= #

# Given two lists of numbers of the same length, create a new list by 
# multiplying the pairs of numbers in corresponding positions in the two lists.

# Example:

# [2, 4, 5] x [2, 3, 6] = [4, 12, 30]

list_one = [2, 4, 5]
list_two = [2, 3, 6]
multiplied_list = []

for i in range(len(list_one)):
    product = list_one[i] * list_two[i]
    multiplied_list.append(product)

print multiplied_list

#  ======================================================================= #
#                              Matrix Addition                             #
#  ======================================================================= #

# Given two two-dimensional lists of numbers of the size 2x2 two dimensional
# list is represented as an list of lists:

# [ [2, -2],
#  [5, 3] ]

# Calculate the result of adding the two matrices. The number in each 
# position in the resulting matrix should be the sum of the numbers in the 
# corresponding addend matrices. Example: 

# to add

# 1 3
# 2 4

# and

# 5 2
# 1 0

# results in

# 6 5
# 3 4

matrix_one = [ [1, 3], [2, 4] ]

matrix_two = [ [5, 2], [1, 0] ]

new_matrix = [ [], [] ]

for i in range(len(matrix_one)):
    for j in range(len(matrix_one[i])):
        total = matrix_one[i][j] + matrix_two[i][j]
        new_matrix[i].append(total)

print new_matrix

#  ======================================================================= #
#                            Matrix Addition II                            #
#  ======================================================================= #

# Use your solution in Matrix Addition, and extend it to work for a pair of
# matrices of any size, as long as they have the same size.

matrix_one = [ [1, 3, 5], [2, 4, 6], [4, 9, 0] ]

matrix_two = [ [5, 2, 8], [1, 0, 2], [1, 0, 2] ]

new_matrix = []

for i in range(len(matrix_one)):
    new_matrix.append([])
    for j in range(len(matrix_one[i])):
        total = matrix_one[i][j] + matrix_two[i][j]
        new_matrix[i].append(total)

print new_matrix

#  ======================================================================= #
#                                   De-dup                                 #
#  ======================================================================= #

# Given a list of numbers or strings, create a new list containing the same
# elements as the first list, except with any duplicate values removed. 
# Print the list.

numbers_list = [4, 5, -2, -3, 11, 1, 8, 3, -2, 4, 8, 1]
de_duped_list = []

for number in numbers_list:
    if number not in de_duped_list:
        de_duped_list.append(number)

print de_duped_list