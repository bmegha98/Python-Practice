'''
Given the first 2 terms A and B of a Geometric Series, tell the Nth term of the series.
'''
import math
if __name__=='__main__':
    T=int(input())
    for i in range(T):
        l=list(map(int,input().split()))
        A,B=l[0],l[1]
        N=int(input())
        r=B/A
        tmp=r**(N-1)
        print(math.floor(A*tmp))
