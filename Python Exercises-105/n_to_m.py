#  ======================================================================= #
#                          Exercises - Python 105                          #
#  ======================================================================= #

# Begin here:

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