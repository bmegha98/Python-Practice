'''
Given a matrix mat[][] of size N x N. The task is to print the elements of the matrix in the snake pattern.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        l = list(input().split())
        A = [l[i:i+N] for i in range(0,N*N,N)]
        for i in range(N):
            if i%2 != 0:
                A[i].reverse()
        for ch in A:print(*ch,end=' ')
        print()
