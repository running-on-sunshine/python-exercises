#  ======================================================================= #
#                          Exercises - Python 105                          #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                                  1 to 10                                 #
#  ======================================================================= #

# Using a for loop and the range function, print out the numbers between 
# 1 and 10 inclusive, one on a line.

for i in range(1, 11):
    print(i)

#  ======================================================================= #
#                                  n to m                                  #
#  ======================================================================= #

# Same as the previous problem, except you will prompt the user for the number 
# to start on and the number to end on.

# Make sure the user does not enter a starting number that is greater than the 
# ending number.

instructions = '''
==========================================
           Let's count numbers! 
==========================================

|----------------------------------------| 
| We will ask for a number to start from |
| and a number to end on.                | 
|----------------------------------------| 

|----------------------------------------|
| Please enter an end number larger than |
| the start number.                      |
|----------------------------------------|
'''

print instructions

start_num_input = raw_input('Start from: ')
start_num = int(start_num_input)

end_num_input = raw_input('End on: ')
end_num = int(end_num_input)

for i in range(start_num, end_num + 1):
    print(i)

#  ======================================================================= #
#                               Odd Numbers                                #
#  ======================================================================= #

# Print each odd number between 1 and 10 inclusive. 

# ----------------------------------------------------------- #
#                       Stepping method                       #
# ----------------------------------------------------------- #

# Uses the stepping within the range. 
# Below states: 'Start at 1, end at 11, stepping by every 2.'

for i in range(1, 11, 2):
    print(i)

# ------------------------------------------------------------ #
#                        Modulus method                        #
#------------------------------------------------------------- #

# Uses the modulus to check if a number is not even. 
# Then, prints it that number. 

for i in range(1, 11):
    if i % 2 != 0:
        print(i)

#  ======================================================================= #
#                             How many coins?                              #
#  ======================================================================= #

# Write a program that will prompt you for how many coins you want. 
# Initially you have no coins. It will ask you if you want a coin? 

# If you type "yes", it will give you one coin, and print out the current tally. 
# If you type no, it will stop the program.

coin_sum = 0

while True:
    print ('You have %d coins') % coin_sum
    add_coin = raw_input("Do you want another ('yes' or 'no')? ")
    if add_coin == 'yes':
        coin_sum += 1
    else:
        print 'Bye'
        break

#  ======================================================================= #
#                             Print a Square                               #
#  ======================================================================= #

# Print a 5x5 square of * characters.

for i in range(5):
    print ('*' * 5)

#  ======================================================================= #
#                            Print a Square II                             #
#  ======================================================================= #

# Print a NxN square of * characters. Prompt the user for N.

size_input = raw_input('How big is the square? ')
size = int(size_input)

for i in range(size):
    print('*' * size)

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

#  ======================================================================= #
#                            Print a Triangle                              #
#  ======================================================================= #

# Print a triangle consisting of * characters.

num = 13
for i in range(1, num + 2, 2):
    total_spaces = num - i
    print(' ' * (total_spaces/2) + '*' * i + ' ' * (total_spaces/2))

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

#  ======================================================================= #
#                           Multiplication Table                           #
#  ======================================================================= #

# Print the multiplication table for numbers from 1 up to 10.

separator = '...'

for i in range(1, 11):
    for j in range(1, 11):
        print i, 'x', j, '=', i * j
    print separator