'''
Given a byte, swap the two nibbles in it. For example 100 is be represented as 01100100 in a byte (or 8 bits). 
The two nibbles are (0110) and (0100). If we swap the two nibbles, we get 01000110 which is 70 in decimal.
'''
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        X=int(input())
        binX=list('{0:08b}'.format(X))
        binY=binX[4:]+binX[0:4]
        Y=int(''.join(binY),2)
        print(Y)
