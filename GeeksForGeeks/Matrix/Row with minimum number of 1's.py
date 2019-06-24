'''
Determine the row index with minimum number of ones. The given 2D matrix has only zeroes and ones and also the matrix is sorted row wise.
If two or more rows have same number of 1's than print the row with smallest index.
Print the index of the row with minimum number of 1's. If there is 0 number of '1' in the matrix then, print '-1'.
'''

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        sizes = list(map(int,input().split()))
        n , m = sizes[0],sizes[1]
        l = list(input().split())
        if all(ch == '0' for ch in l):print(-1)
        else :
            A = [''.join(l[i:i+m]) for i in range(0,n*m,m)]
            Min = n*m
            ind = -1
            for i in range(n):
                c = A[i].count('1')
                if c!=0 and c < Min:
                    Min= c
                    ind = i
            print(ind)
                
