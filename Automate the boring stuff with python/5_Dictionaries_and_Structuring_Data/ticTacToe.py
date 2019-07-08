from random import randint
Board = {1 :' ' , 2 : ' ' , 3 : ' ',
         4 :' ' , 5 : ' ' , 6 : ' ',
         7 :' ' , 8 : ' ' , 9 : ' ',
        }

possiblemoves = [i for i in range(1,10)]

def printBoard():
    print()
    print(' '+Board[1]+' | '+Board[2]+' | '+Board[3])
    print('---+---+---')
    print(' '+Board[4]+' | '+Board[5]+' | '+Board[6])
    print('---+---+---')
    print(' '+Board[7]+' | '+Board[8]+' | '+Board[9])
    print()
    
    
def IsWinner(turn):
    return any([Board[1] == turn and Board[2] == turn and Board[3] == turn,
               Board[4] == turn and Board[5] == turn and Board[6] == turn,
               Board[7] == turn and Board[8] == turn and Board[9] == turn,
               Board[1] == turn and Board[4] == turn and Board[7] == turn,
               Board[2] == turn and Board[5] == turn and Board[8] == turn,
               Board[3] == turn and Board[6] == turn and Board[9] == turn,
               Board[1] == turn and Board[5] == turn and Board[9] == turn,
               Board[3] == turn and Board[5] == turn and Board[7] == turn])

def PlayerMove():
    move = 0
    while move not in possiblemoves:
        move = int(input('Your turn! \n  Select position among these --> '+('/'.join(str(x) for x in possiblemoves))+' : '))
    possiblemoves.remove(move)
    Board[move] = turn

def ComputerMove(player):
    print("Computer's turn --->")
    pos = 0
    for x in possiblemoves:
        Board[x] = turn
        if IsWinner(turn):
            pos = x
            Board[x]= ' '
            break
        
        Board[x] = player
        if IsWinner(player):
            pos = x
            Board[x]= ' '
            break
       
        Board[x] = ' '
        
    if pos:
        move = pos
    else :
        move = possiblemoves[randint(0,len(possiblemoves)-1)]
    possiblemoves.remove(move)
    Board[move] = turn 
            
    
    

if __name__ == '__main__':

    print('------ Welcome to tic-tac-toe game ------ !')
    name = input('Enter Your good name :)  ')
    player = ''
    while player == '' or( player!='X' and player !='O'):
        player = input('Select your symbol (X / O) :  ').upper()

    if player == 'X' : computer = 'O'
    else : computer = 'X'

    turn = ['X','O'][randint(0,1)]

    if turn == player : print('Aha! You will go first :)')
    else : print('Computer will go first :|')

    while True:
        if len(possiblemoves) == 0 : break
    
        if turn == player : PlayerMove()
        else: ComputerMove(player)
        printBoard()
        if IsWinner(turn): break
        if turn == player : turn = computer
        else : turn = player

    if IsWinner(turn) and turn == player : print('Congratulations',name,'!! You Won yeahh :)')
    elif IsWinner(turn) and turn == computer : print("Don't loose hope",name,"Better luck next time :(")
    else : print('OMG !! This is draw :|')
        
        
                                                                           

             
