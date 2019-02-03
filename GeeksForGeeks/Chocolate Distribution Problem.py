'''
//MEMORY ERROR
from itertools import permutations
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        A=list(map(int,input().split()))
        M=int(input())
        A.sort()
        if M==1:print('0')
        else:
            lst=[]
            l=list(permutations(A,M))
            for ch in l:
                ch=list(ch)
                ch.sort()
                lst.append(ch[-1]-ch[0])
            print(min(lst))
'''
import sys
def MinimumDifference(arr,n,m):
    if n==0 or m==0 or m==1:
        return 0
    if m>n:return -1
    arr.sort()
    i=0
    first,last=0,0
    min_diff=sys.maxsize
    while i+m-1<n:
        diff=arr[i+m-1]-arr[i]
        if diff<min_diff:
            min_diff=diff
            first=i
            last=(i+m-1)
        i+=1
    return arr[last]-arr[first]

if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        A=list(map(int,input().split()))
        M=int(input())
        print(MinimumDifference(A,N,M))
