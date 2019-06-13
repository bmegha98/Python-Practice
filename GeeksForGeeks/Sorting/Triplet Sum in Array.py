'''
Given an array A[] of N numbers and another number x, determine whether or not there exist three elements in A[] whose sum is exactly x.
Print 1 if there exist three elements in A whose sum is exactly x, else 0.
'''

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        NX = list(map(int,input().split()))
        A = sorted(list(map(int,input().split())))
        n , x = NX[0] , NX[1]
        flag = 0
        last = -1
        for i in range(n-1,-1,-1):
            if A[i]<x:
                last = i
                break
        while last>2:
            rest = x - A[last]
            low = 0
            high = last-1
            while low<high:
                if A[low]+A[high] == rest:
                    flag = 1
                    break
                elif A[low]+A[high] > rest :
                    high-=1
                else :
                    low+=1
            last-=1
        
        print(flag)
