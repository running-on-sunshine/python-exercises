#  ======================================================================= #
#                          Exercises - Python 103                          #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                              Tip Calculator 2                            #
#  ======================================================================= #

# Allow the ability to divide the check into a equal parts amount a number of people. 
# The user will enter the number of people to be divided amongst.

bill = float(raw_input('Total bill amount? $'))
service = raw_input('Level of service (good, fair, bad)? ')
split_number = float(raw_input('Split how many ways? '))

tip_percent = 0

if service == 'good':
    tip_percent = 0.20
elif service == 'fair':
    tip_percent = 0.15 
elif service == 'bad':
    tip_percent = 0.10

tip = bill * tip_percent 
total = bill + tip
split_bill = total / split_number

tip_amount = 'Tip amount: $%.2f' % tip
total_amount = 'Total amount: $%.2f' % total
per_person_amount = 'Amount per person: $%.2f' % split_bill

print tip_amount
print total_amount
print per_person_amount

# ============ Could also print like this: =================
# print "Tip amount: $%s" % format(tip, '.2f')
# print "Total amount: $%s" % format(total_bill, '.2f')
# print "Amount per person: $%s" % format(split_bill, '.2f')