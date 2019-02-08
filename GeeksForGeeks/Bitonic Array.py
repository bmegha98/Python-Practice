'''
Given an array A[0 … n-1] containing n positive integers, a subarray A[i … j] is bitonic if there is a k with i < k < j such that 
A[i] < A[i + 1] ... < A[k] > A[k + 1] > .. A[j – 1] >  A[j]. Write a program that returns the length of the maximum length bitonic subarray.
For Example: In array {20, 4, 1, 2, 3, 4, 2, 10} the maximum length bitonic subarray is {1, 2, 3, 4, 2} which is of length 5.
Note: A[k] can be first or last element. Ex:-  10 20 30 , 30 20 10 and 1 2 3 4 3 2 1 these all are bitonic array.
'''
def Bitonic(n,a):
    inc=[1]*n
    dec=[1]*n
    inc[0]=1
    dec[0]=1
    for i in range(1,n):
        if a[i]>a[i-1]:
            inc[i]=inc[i-1]+1
        else:
            inc[i]=1
    for i in range(n-2,-1,-1):
        if a[i]>a[i+1]:
            dec[i]=dec[i+1]+1
        else:
            dec[i]=1
    Max=inc[0]+dec[0]-1
    for i in range(1,n):
        if inc[i]+dec[i]-1 > Max:
            Max=inc[i]+dec[i]-1
    
    return Max
    
    
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        A=list(map(int,input().split()))
        print(Bitonic(N,A))
