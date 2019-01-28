'''
Check whether the number is Triangular or not. A number is termed as triangular number if we can represent it in the form of triangular 
grid of points such that the points form an equilateral triangle and each row contains as many points as the row number, i.e., the first 
row has one point, second row has two points, third row has three points and so on. 
The starting triangular numbers are 1, 3 (1+2), 6 (1+2+3), 10 (1+2+3+4).
'''
if __name__=='__main__':
    T=int(input())
    for i in range(T):
        N=int(input())
        sum=0
        for j in range(1,N+1):
            sum+=j
            if sum==N:
                print('1')
                break
            elif sum>N:
                print('0')
                break
