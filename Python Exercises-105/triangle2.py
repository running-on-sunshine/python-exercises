#  ======================================================================= #
#                          Exercises - Python 105                          #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                           Print a Triangle II                            #
#  ======================================================================= #

# Given a number as the height, print a triangle as in "Print a Triangle" 
# but with the given height.

height_input = raw_input('Enter a height: ')
height = int(height_input)

width = 2 * (height - 1) + 1

for i in range(1, width + 2, 2):
    total_spaces = width - i
    print(' ' * (total_spaces/2) + '*' * i + ' ' * (total_spaces/2))