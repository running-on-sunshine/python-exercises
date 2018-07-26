#  ======================================================================= #
#                             String Exercises                             #
#  ======================================================================= #

# Begin here:

#  ======================================================================= #
#                             Capitalize a String                          #
#  ======================================================================= #

# Given a string, print the string capitalized. #string #easy

string = raw_input('Enter a message: ')
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
capitalized_string = ''

for i in range(len(string)):
    letter = string[i]
    if i == 0 and string[i] in lowercase:
        for j in range(len(lowercase)):
            if string[i] == lowercase[j]:
                letter = uppercase[j]
                break
    elif (string[i - 1] in lowercase) or (string[i - 1] in uppercase):
        letter = string[i]
    else:
        for j in range(len(lowercase)):
            if string[i] == lowercase[j]:
                letter = uppercase[j]
                break
                
    capitalized_string += letter 

print capitalized_string