'''
Given a matrix mat[] of size n x m, where every row and column is sorted in increasing order, and a number x is given. The task is to find
whether element x is present in the matrix or not.

Expected Time Complexity : O(m + n)
'''

def BinarySearch(low,high,arr,ele):
    m = (low+high)//2
    if low>high : return 0
    if arr[m] == ele : return 1
    elif arr[m]>ele : return BinarySearch(low,m-1,arr,ele)
    else : return BinarySearch(m+1,high,arr,ele)
    
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        size = list(map(int,input().split()))
        n , m = size[0] , size[1]
        arr = list(map(int,input().split()))
        x = int(input())
        matrix = [arr[i:i+m] for i in range(0,n*m,m)]
        res = 0
        for ch in matrix :
            if BinarySearch(0,m-1,ch,x): 
                res = 1
                break
        print(res)
            
        
