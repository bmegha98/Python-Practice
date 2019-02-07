'''
You are given an array A of size N. You need to find all pairs in the array that sum to a number K. If no such pair exists then output 
will be -1. The elements of the array are distinct and are in sorted order.
Note: (a,b) and (b,a) are considered same. Also, an element cannot pair with itself, i.e., (a,a) is invalid.
'''
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        A=list(map(int,input().split()))
        K=int(input())
        i=0
        c=0
        j=len(A)-1
        while i!=j:
            if A[i]+A[j]==K:
                print(A[i],A[j],K)
                c+=1
                i+=1
            elif A[i]+A[j]>K:
                j-=1
            else:
                i+=1
        if c==0:print('-1')
