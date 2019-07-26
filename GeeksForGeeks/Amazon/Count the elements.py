'''
Given two arrays A and B. Given Q queries each having a positive integer i denoting an index of the array A.
For each query, your task is to find all the elements less than or equal to Ai in the array B.
'''

def BinarySearch(low,high,A,ele):
    while low<= high :
        mid = (low + high)//2
        if A[mid] <= ele :
            low = mid+1
        else:
            high = mid-1;
    return high
    
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))
        B.sort()
        Q = int(input())
        for q in range(Q):
            ind = int(input())
            searchind = BinarySearch(0,n-1,B,A[ind])
            print(searchind+1)
