#  ======================================================================= #
#                          Exercises - Python 105                          #
#  ======================================================================= #

# Begin here:

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