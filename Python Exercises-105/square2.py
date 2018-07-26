#  ======================================================================= #
#                          Exercises - Python 105                          #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                            Print a Square II                             #
#  ======================================================================= #

# Print a NxN square of * characters. Prompt the user for N. 

size_input = raw_input('How big is the square? ')
size = int(size_input)

for i in range(size):
    print('*' * size)