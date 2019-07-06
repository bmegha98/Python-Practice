from random import randint
if __name__ == '__main__':
    print('Hello player! Welcome to Guess The Number Game :) ')
    choice = 'Yes'
    while choice in ['Yes' , 'yes' , 'y' ,'Y']:
        name = input('Enter your name :  ')
        secretnum = randint(1,30)
        print('I am thinking of a number between 1 and 30')
        num ,chances = 0 , 0
        for chances in range(1,10):
            print('Take a guess.')
            num = int(input())
            if num < secretnum :  print('OOPS! Your guess is too low.')
            elif num > secretnum : print('OOPS! Your guess is too high.')
            else :
                break

        if num == secretnum :
            print('Good job! You guessed my number in ',chances,' guesses!')
        else :
            print('Nope . The number I was thinking of was ',secretnum)

        choice = input('Do you want to play again ?(Type yes for play) ')

    
