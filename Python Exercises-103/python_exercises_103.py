#  ======================================================================= #
#                          Exercises - Python 103                          #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                             Day of the Week                              #
#  ======================================================================= #

# Given the following code that prompts the user for a day number, the user
# will enter a number between 0 to 6 inclusive.

# Given this number, print a day of the week. 
# 0 for Sunday, 1 for Monday, 2 for Tuesday, and so on.

# The 'int' function converts a numeric string to a number. 

day_input = raw_input('Day of the week (0-6)? ')
day = int(day_input)
day_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day_message = 'That day is ' + day_of_week[day] + '.'

print day_message

#  ======================================================================= #
#                            Work or Sleep In?                             #
#  ======================================================================= #

# Prompt the user for a day of the week just like the previous problem. 
# Except this time print "Go to work" if it's a work day and "Sleep in" 
# if it's a weekend day.

day_input = (raw_input('Which day is it today (0-6)? '))
day = int(day_input)

work_message = '''
                We're going to work.
                Let's make today a great day! 
                Let's make things happen! :)
                '''
sleep_in_message = '''
                We get to sleep in. zzZzz...Yay!
                Go ahead. Hit that snooze button. ;)
                '''

if 5 >= day >= 1:
        print work_message
else:
        print sleep_in_message

#  ======================================================================= #
#                           Celsius to Fahrenheit                          #
#  ======================================================================= #

# Prompt the user for a number in degrees Celsius, and convert the value to 
# degrees in Fahrenheit and display it to the user. 

celsius_input = (raw_input("Temperature in C? "))
celsius = float(celsius_input)
fahrenheit = celsius * 9/5 + 32
temp_conversion = '%s F' % fahrenheit

print temp_conversion

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