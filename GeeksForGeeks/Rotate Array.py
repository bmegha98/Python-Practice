'''
Given an array of size N, rotate it by D elements. 
'''
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        l=list(map(int,input().split()))
        N,K=l[0],l[1]
        A=list(map(int,input().split()))
        rotate=A[K:]+A[0:K]
        print(' '.join(str(x) for x in rotate))
