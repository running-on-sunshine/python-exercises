#  ======================================================================= #
#                          Exercises - Python 105                          #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                              Print a Box                                 #
#  ======================================================================= #

# Given a height and width, input by the user, print a box consisting of * 
# characters as its border.

width_input = raw_input('Width? ')
width = int(width_input)

height_input = raw_input('Height? ')
height = int(height_input)

def print_box(width, height):       
    for i in range(height):
        if i == 0 or i == (height-1):
            print ('*' * width)
        else: 
            print('*' + ' ' * (width-2) + '*')

print_box(width, height)

# ------------------------- Explanation: ----------------------------- #
# If index of height is 0 (first line) or index of height is height-1  #
# (last line), we want to print the full value of width.               #
#                                                                      #
# Else, everything that is not the first or last value of height,      #
# we want to print & concatonate.                                      #
# -------------------------------------------------------------------- #