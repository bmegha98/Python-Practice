'''
//TLE
import numpy  
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        Arr=list(map(int,input().split()))
        P=[1]*(N)
        l=[ch for ch in Arr]
        for i in range(N):
            l[i]=1
            P[i]=numpy.prod(l)
            l[i]=Arr[i]
        print(*P)
'''
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        Arr=list(map(int,input().split()))
        P=[1]*N
        lft=[1]*N
        right=[1]*N
        tmp=1
        for i in range(N):
            lft[i]=tmp
            tmp*=Arr[i]
        tmp=1
        for i in range(N-1,-1,-1):
            right[i]=tmp
            tmp*=Arr[i]
        for i in range(N):
            P[i]=lft[i]*right[i]
        print(*P)
            
