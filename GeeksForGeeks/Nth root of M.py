'''
You are given 2 numbers (N , M); the task is to find N√M (Nth root of M).
'''
import math
if __name__=='__main__':
    T=int(input())
    for i in range(T):
        l=list(map(int,input().split()))
        N,M=l[0],l[1]
        s=round(M**(1/N))
        if s**N==M:print(int(s))
        else:print('-1')
