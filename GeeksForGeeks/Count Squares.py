'''
Given a sample space S consisting of all perfect squares starting from 1, 4, 9 and so on. 
You are given a number N, you have to print the number of integers less than N in the sample space S.
'''
from math import sqrt,floor
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        if sqrt(N)==int(sqrt(N)):print(floor(sqrt(N))-1)
        else:print(floor(sqrt(N)))
            
