'''
Given an array of N positive integers. Your task is to find the GCD of all numbers of the array.
'''
def GCD(A,B):
    if A==0:return B
    if B==0:return A
    if A==B:return A
    if A>B:return GCD(B,A%B)
    if A<B:return GCD(A,B%A)
    
if __name__=='__main__':
    T=int(input())
    for i in range(T):
        N,Array=int(input()),list(map(int,input().split()))
        res=Array[0]
        for i in range(1,N):
            res=GCD(res,Array[i])
        print(res)
