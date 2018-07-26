#  ======================================================================= #
#                             String Exercises                             #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                             Uppercase a String                           #
#  ======================================================================= #

# Given a string, print the string uppercased. #string #easy

string = raw_input('Enter a message: ')
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
uppercased_string = ''

for letter in string:
    for i in range(len(lowercase)): 
        lowerletter = lowercase[i]
        if lowerletter == letter:
            letter = uppercase[i]
            break
    
    uppercased_string += letter

print uppercased_string