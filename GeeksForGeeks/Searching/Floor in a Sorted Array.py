'''
Given a sorted array arr[] of size N without duplicates, and given a value x. Find the floor of x in given array. 
Floor of x is defined as the largest element K in arr[] such that K is smaller than or equal to x.
Output the index of floor of x if exists, else print -1.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        Nx = list(map(int,input().split()))
        N , x = Nx[0] , Nx[1]
        array = list(map(int,input().split()))
        res = -1
        for i in range(N-1,-1,-1):
            if array[i]<=x:
                res = i
                break
        
        print(res)
