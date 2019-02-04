'''
Given an array A of positive integers. Count number of smaller elements on right side of each array.
'''
def SmallerCount(arr,n):
    for i in range(n):
        c=0
        val=arr[i]
        newarr=arr[i+1:]
        for k in newarr:
            if k<val:
                c+=1
        print(c,end=' ')
    print()
        
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        Arr=list(map(int,input().split()))
        SmallerCount(Arr,N)
        
