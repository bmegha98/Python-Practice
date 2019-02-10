'''
Given an array A of N non-negative integers representing height of blocks at index i as Ai where the width of each block is 1. 
Compute how much water can be trapped in between blocks after raining.
Structure is like below:
|  |
|__|
'''
def findWater(arr, n): 
    left = [0]*n 
    right = [0]*n 
    water = 0
    left[0] = arr[0] 
    for i in range( 1, n): 
        left[i] = max(left[i-1], arr[i]) 
  
    right[n-1] = arr[n-1] 
    for i in range(n-2, -1, -1): 
        right[i] = max(right[i+1], arr[i]); 

    for i in range(0, n): 
        water += min(left[i],right[i]) - arr[i] 
  
    return water 
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        A=list(map(int,input().split()))
        print(findWater(A,N))
        
