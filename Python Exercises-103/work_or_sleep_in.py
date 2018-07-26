#  ======================================================================= #
#                          Exercises - Python 103                          #
#  ======================================================================= #

# Begin here:

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