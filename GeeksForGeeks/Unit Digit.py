'''
Given a number N. The task is to find the unit digit of factorial of given number N.
'''
def Factorial(N):
    if N==0 or N==1:
        return 1
    else:
        return N*Factorial(N-1)
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        if N<5:
            fact=Factorial(N)
            print(fact%10)
        else:
            print('0')
    
