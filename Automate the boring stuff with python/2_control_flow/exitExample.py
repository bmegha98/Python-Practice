import sys
if __name__ == '__main__':
    while True:
        print('Type exit to exit')
        response = input()
        if response == 'exit':
            sys.exit()
        print('You typed '+ response +' .')
