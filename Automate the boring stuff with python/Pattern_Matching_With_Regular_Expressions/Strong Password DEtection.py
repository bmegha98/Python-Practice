'''
    1. at least eight characters long
    2. contains both uppercase and lowercase characters
    3. has at least one digit.
'''

import re

pass_length_regex = re.compile(r'.{8,}')

pass_upper_regex = re.compile(r'[A-Z]')

pass_lower_regex = re.compile(r'[a-z]')

pass_digit_regex = re.compile(r'[0-9]')



def PasswordDetection(pw):

    if pass_length_regex.search(pw) == None:
        return False
    
    if pass_upper_regex.search(pw) == None:
        return False
    
    if pass_lower_regex.search(pw) == None:
        return False
    
    if pass_digit_regex.search(pw) == None:
        return False
    
    else:
        return True
   

if __name__ == '__main__':

    print('**********************Password Checker****************************')

    password = input('Enter password -->  ')
    if PasswordDetection(password):
        print('Your password is strong :)')
    else:
        print('Your password is weak :( Make it again !')

