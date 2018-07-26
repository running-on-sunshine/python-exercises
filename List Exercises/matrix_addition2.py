#  ======================================================================= #
#                             List Exercises                               #
#  ======================================================================= #

# Begin here:

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