#  ======================================================================= #
#                             List Exercises                               #
#  ======================================================================= #

# Begin here:

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

# ============ ALTERNATE VERSION ============

# width = len(r[0])
# height = len(r)

# for i in range(height):
#     for j in range(len(width)):
#         r[i][j]= m1[i][j] = m2[i][j]
# print r

# ----------------------------------------------------------------- #
#                     Turn this into a function                     #
# ----------------------------------------------------------------- #

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