#!python3
# pw.py - An insecure password locker program.
import sys, pyperclip

Passwords = {'gmail': 'xyz123',
             'blog' : 'abc007',
             'luggage' : 12345
             }
'''
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]  # first command line arg is the account name
'''

if __name__ == '__main__':
    print('********************PASSWORD LOCKER***********************')
    account = ''
    while account == '':
        account = input('Enter account name :  ')    
    if account in Passwords:
        pyperclip.copy(Passwords[account])
        print('Password for '+ account + ' copied to clipboard.')
    else:
        print('There is no account named ' + account)
