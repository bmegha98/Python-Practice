'''
Given an integer array and a non-negative integer k, count all distinct pairs with difference equal to k, i.e., A[ i ] - A[ j ] = k.
In each separate line print the number of times difference k exists between the elements of the array.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = sorted(list(map(int,input().split())))
        K = int(input())
        count = 0
        l = []
        for i in range(N-1):
            ch = A[i]+K
            if ch in A[i+1:] and (A[i],ch) not in l:
                count+=1
                l.append((A[i],ch))
        print(count)
