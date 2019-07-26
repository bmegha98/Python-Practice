'''
Given an array of elements which is first increasing and then may be decreasing, find the maximum element in the array.
Note: If the array is increasing then just print then last element will be the maximum value.
'''
if __name__ == '__main__':
    
    t = int(input())
    while t>0:
        n = int(input())
        A = list(map(int,input().split()))
        A.sort()
        print(A[n-1])
            
        t -= 1
