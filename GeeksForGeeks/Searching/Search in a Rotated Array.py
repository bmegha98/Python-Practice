'''
Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element K. 
The task is to find the index of the given element K in the array A.
Corresponding to each test case, output the index of the element found in the array.  If element is not present, then output -1.
'''

def Pivot(arr):
    p = len(arr)-1
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            p = i
            break
    return p

def BinarySearch(arr , l, h,x):
    m = (l+h)//2
    if l>h : return -1
    if arr[m] == x: return m
    elif arr[m] <x : return BinarySearch(arr , m+1 , h , x)
    else : return BinarySearch(arr , l , m-1 , x)
            
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        array = list(map(int,input().split()))
        K = int(input())
        piv = Pivot(array)
        if array[piv] == K : print(piv)
        elif BinarySearch(array,0,piv-1,K) != -1:
            print(BinarySearch(array,0,piv-1,K))
        elif BinarySearch(array , piv+1 , N-1 ,K)!= -1:
            print(BinarySearch(array , piv+1 , N-1 ,K))
        else : print(-1)
            
