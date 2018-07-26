#  ======================================================================= #
#                       List Exercises... revisited                        #
#  ======================================================================= #

# Begin here:

# Turn everything into a function! 

#  ======================================================================= #
#                             Sum the Numbers                              #
#  ======================================================================= #

# Given a list of numbers, print their sum. When I say given something, 
# just make something up and store it in a variable.

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

#  ======================================================================= #
#                              Largest Number                              #
#  ======================================================================= #

# Given a list of numbers, print the largest of the numbers.

# Turn this into a function: take one argument (a list of numbers) and 
# return the largest.

def find_largest_num(list):
    largest_num = list[0]
    for number in list:
        if number > largest_num:
            largest_num = number

    return largest_num

numbers = [-4, 5, -11, 1, -4]

result = find_largest_num(numbers)

print result

#  ======================================================================= #
#                              Smallest Number                             #
#  ======================================================================= #

# Given a list of numbers, print the smallest of the numbers.

# Turn this into a function.

def find_smallest_num(list):
    smallest_num = list[0]
    for number in list:
        if number < smallest_num:
            smallest_num = number

    return smallest_num

numbers = [4, 5, 11, -8, 4]

result = find_smallest_num(numbers)

print result

#  ======================================================================= #
#                               Even Numbers                               #
#  ======================================================================= #

# Given a list of numbers, print each number in the list that is even.

# Turn this into a function: take one argument (list of numbers) and return 
# a new list with just the even numbers.

def print_even_num(list):
    even_numbers = []
    for number in list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers
            
numbers = [4, 5, 11, 1, 8, 3]

result = print_even_num(numbers)

print result

#  ======================================================================= #
#                              Positive Numbers                            #
#  ======================================================================= #

# Given a list of numbers, print each number in the list that is greater 
# than zero.

# Turn this into a function: take one argument (list of numbers) and return
# a new list with just the numbers greater than zero.

def print_positive_num(list):
    for number in list:
        if number > 0:
            print number
            
numbers = [4, 5, -2, -3, 11, 1, 8, 3]

print_positive_num(numbers)

#  ======================================================================= #
#                             Positive Numbers II                          #
#  ======================================================================= #

# Given a list of numbers, create a new list which contains every number in
# the given list which is positive.

# Turn this into a function, similar to the prior exercises.

def create_positive_num_list(list):
    positive_numbers = []
    for number in list:
        if number > 0:
            positive_numbers.append(number)

    return positive_numbers
            
numbers = [4, 5, -2, -3, 11, 1, 8, 3]

result = create_positive_num_list(numbers)

print result

#  ======================================================================= #
#                             Multiply a List                              #
#  ======================================================================= #

# Given a list of numbers, and a single factor (also a number), create a 
# new list consisting of each of the numbers in the first list multiplied 
# by the factor. Print the new list out to the screen.

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

#  ======================================================================= #
#                             Multiply Vectors                             #
#  ======================================================================= #

# Given two lists of numbers of the same length, create a new list by 
# multiplying the pairs of numbers in corresponding positions in the two lists.

# Example:

# [2, 4, 5] x [2, 3, 6] = [4, 12, 30]

# Turn the rest of these exercises into functions. It's up to you to figure out
# how many arguments the function needs!

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

def add_matrices(matrix_one, matrix_two):
    new_matrix = [ [], [] ]
    for i in range(len(matrix_one)):
        for j in range(len(matrix_one[i])):
            total = matrix_one[i][j] + matrix_two[i][j]
            new_matrix[i].append(total)
    
    return new_matrix

matrix_one = [ [1, 3], [2, 4] ]

matrix_two = [ [5, 2], [1, 0] ]

result = add_matrices(matrix_one, matrix_two)

print result

#  ======================================================================= #
#                                   De-dup                                 #
#  ======================================================================= #

# Given a list of numbers or strings, create a new list containing the same
# elements as the first list, except with any duplicate values removed. 
# Print the list.

def remove_duplicates(list):
    de_duped_list = []
    for number in list:
        if number not in de_duped_list:
            de_duped_list.append(number)
    return de_duped_list

numbers = [4, 5, -2, -3, 11, 1, 8, 3, -2, 4, 8, 1]

result = remove_duplicates(numbers)

print result