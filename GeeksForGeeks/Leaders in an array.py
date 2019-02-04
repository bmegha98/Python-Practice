'''
Given an array of positive integers.
Your task is to find the leaders in the array.
Note: An element of array is leader if it is greater than or equal to all the elements to its right side. 
Also, the rightmost element is always a leader. 
'''
def Leaders(A,n):
    Max=A[n-1]
    S=[Max]
    for i in range(n-2,-1,-1):
        if A[i]>=Max:
            S.append(A[i])
            Max=A[i]
    print(*S[::-1])
    
T=int(input())
for _ in range(T):
    n=int(input())
    A=list(map(int,input().split()))
    Leaders(A,n)
            
