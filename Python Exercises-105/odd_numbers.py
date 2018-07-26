#  ======================================================================= #
#                          Exercises - Python 105                          #
#  ======================================================================= #

# Begin here:

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