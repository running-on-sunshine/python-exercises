#  ======================================================================= #
#                          Exercises - Python 103                          #
#  ======================================================================= #

# Begin here:

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