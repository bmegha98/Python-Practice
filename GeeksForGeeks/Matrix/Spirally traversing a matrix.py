'''
Given a matrix mat[][] of size M*N. Traverse and print the matrix in spiral form.
'''

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        size = list(map(int,input().split()))
        m , n = size[0],size[1]
        arr = list(input().split())
        matrix = [arr[i:i+n] for i in range(0,n*m,n)]
        
        i = 0
        j = 0
        while i < m and j < n:
            for k in range(j,n):
                print(matrix[i][k],end = ' ')
            i+=1
            
            for k in range(i,m):
                print(matrix[k][n-1],end= ' ')
            n-=1
            
            if i<m:
                for k in range(n-1,j-1,-1):
                    print(matrix[m-1][k],end= ' ')
                m-=1
            
            if j<n:
                for k in range(m-1,i-1,-1):
                    print(matrix[k][j],end = ' ')
                j+=1
        print()
            
