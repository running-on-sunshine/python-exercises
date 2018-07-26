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
#                       Alternate Version : If...Else                      #
#  ======================================================================= #

day_input = day = raw_input('Day (0-6)? ')
day = int(day_input)

day_of_week = ''

if day == 0:
    day_of_week = 'Sunday'
elif day == 1:
    day_of_week = 'Monday'
elif day == 2:
    day_of_week = 'Tuesday'
elif day == 3:
    day_of_week = 'Wednesday'
elif day == 4:
    day_of_week = 'Thursday'
elif day == 5:
    day_of_week = 'Friday'
elif day == 6:
    day_of_week = 'Saturday'

print day_of_week

#  ======================================================================= #
#                     Alternate Version : Dictionary                       #
#  ======================================================================= #

day_input = day = raw_input('Day (0-6)? ')
day = int(day_input)

day_of_week = {
    0 : 'Sunday',
    1 : 'Monday',
    2 : 'Tuesday',
    3 : 'Wednesday',
    4 : 'Thursday',
    5 : 'Friday',
    6 : 'Saturday',
}

print day_of_week[day]