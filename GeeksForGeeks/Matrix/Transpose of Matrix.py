'''
Write a program to find transpose of a square matrix mat[][] of size N*N.
Transpose of a matrix is obtained by changing rows to columns and columns to rows.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        l = list(input().split())
        A = [l[i:i+N] for i in range(0,N*N,N)]
        B = []
        for i in range(N):
            for j in range(N):
                B.append(A[j][i])
        print(*B)
            
