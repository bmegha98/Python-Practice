'''
Given an array A of positive integers. The task is to find the maximum of j - i subjected to the constraint of A[i] <= A[j].
'''
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        A=list(map(int,input().split()))
        i=0
        Max=0
        while i<N-1:
            for j in range(N-1,i,-1):
                if A[i]<=A[j]:
                    Max=max(Max,j-i)
                    break
            i+=1
        print(Max)
