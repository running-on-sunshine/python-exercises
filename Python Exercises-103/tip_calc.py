#  ======================================================================= #
#                          Exercises - Python 103                          #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                              Tip Calculator                              #
#  ======================================================================= #

# Prompt the user for two things:

# 1. The total bill amount
# 2. The level of service, which can be one of the following: good, fair, or bad

# Calculate the tip amount and the total amount (bill amount + tip amount). 
# The tip percentage based on the level of service is based on:

# good -> 20%
# fair -> 15%
# bad -> 10%

bill = float(raw_input('Total bill amount? $'))
service = raw_input('Level of service (good, fair, bad)? ')

tip_percent= 0

if service == 'good':
    tip_percent = 0.20
elif service == 'fair':
    tip_percent = 0.15
elif service == 'bad':
    tip_percent = 0.10

tip = bill * tip_percent
total = bill + tip

tip_amount = 'Tip amount: $%.2f' % tip
total_amount = 'Total amount: $%.2f' % total

print tip_amount
print total_amount