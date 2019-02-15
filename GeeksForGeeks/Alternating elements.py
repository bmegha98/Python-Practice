'''
Given two arrays A and B of size N and M.
The task is to print the array elements of A and B alternatively, i.e, A[i], B[i], A[i+1], B[i+1] ... .
'''
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        size=list(map(int,input().split()))
        N,M=size[0],size[1]
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        l=[]
        i,j=0,0
        while i<N and j<M:
            l.append(A[i])
            i+=1
            l.append(B[j])
            j+=1
        while i<N:
            l.append(A[i])
            i+=1
        while j<M:
            l.append(B[j])
            j+=1
        print(*l)
