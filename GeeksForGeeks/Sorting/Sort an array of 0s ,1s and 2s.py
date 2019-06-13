'''
Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        low ,mid ,high = 0 ,0 ,N-1
        while mid <= high:
            if A[mid] == 0:
                A[mid],A[low] = A[low],A[mid]
                low+=1
                mid+=1
                
            elif A[mid] == 2:
                A[mid],A[high] = A[high],A[mid]
                high-=1
            else :
                mid+=1
        print(*A)
