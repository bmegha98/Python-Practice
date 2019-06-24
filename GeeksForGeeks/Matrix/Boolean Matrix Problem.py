'''
Given a boolean matrix mat[M][N] of size M X N, modify it such that if a matrix cell mat[i][j] is 1 (or true) then make all the cells of 
ith row and jth column as 1.
'''

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        size = list(map(int,input().split()))
        r , c = size[0],size[1]
        matrix = []
        for i in range(r):
            matrix.append(list(map(int,input().split())))
        
        row , col = [0]*r , [0]*c
        for i in range(r):
            for j in range(c):
                if matrix[i][j]:
                    row[i] =1
                    col[j] = 1
        
        for i in range(r):
            for j in range(c):
                if row[i]==1 or col[j]==1:matrix[i][j]=1
        
        for ch in matrix : print(*ch)
