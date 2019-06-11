'''
This is the time of Christmas and Santa wants to distribute gifts to M children. He has N number of boxes, and each box contains some 
chocolates. Now, Santa wants to distribute N boxes to M children keeping in mind that distribution should be as fair as possible. 
To fairly distribute the gift boxes, Santa wants to minimize the maximum number of choclates gifted to a child.

Formally, given M number of children and N boxes, where each box contains some amount of chocolates. The task is to minimize the maximum 
number of chocolate gifted to a child.

For each testcase, print the minimum number of maximum chocolate a child get.
'''
import sys,math
def Possible(arr,n,m,curr_min):
    children = 1
    curr_sum = 0
    for i in range(n):
        if arr[i] > curr_min :
            return False
        
        if curr_sum+arr[i] > curr_min:
            children+=1
            curr_sum = arr[i]
            if children > m:
                return False
        
        else :
            curr_sum+=arr[i]
    
    return True
    
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        C = list(map(int,input().split()))
        M = int(input())
        start = 0
        end = sum(C)
        res = sys.maxsize
        while start<=end:
            mid = math.floor((start+end)/2)
            if Possible(C,N,M,mid):
                res = min(res,mid)
                end = mid-1
            else :
                start = mid+1
        
        print(res)
