'''
Given a matrix C of size N x M. You are given position of submatrix as X1, Y1 and X2, Y2 inside the matrix. 
Find the sum of all elements inside that submatrix.
'''

if __name__ =='__main__':
    t = int(input())
    for _ in range(t):
        size = list(map(int,input().split()))
        n , m = size[0],size[1]
        l = list(map(int,input().split()))
        matrix = [[l[j] for j in range(i,i+m)] for i in range(0,n*m,m)]
        
        s = list(map(int,input().split()))
        x1 , y1 , x2, y2 = s[0]-1,s[1]-1,s[2]-1,s[3]-1
        
        Sum = 0
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                Sum += matrix[i][j]
                
        print(Sum)
        
