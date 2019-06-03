'''
The cost of stock on each day is given in an array A[] of size N. Find all the days on which you buy and sell the stock so that in between
those days your profit is maximum.
*Input: 
First line contains number of test cases T. First line of each test case contains an integer value N denoting the number of days, followed
by an array of stock prices of N days. 

*Output:
For each testcase, output all the days with profit in a single line. And if there is no profit then print "No Profit".
'''
if __name__ == '__main__':
    T= int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        i = 0
        while i < N:
            start = i 
            for j in range(i,N):
                if j== (N-1) or A[j+1] <= A[j]: break
            
            i = j+1
                
            if i - start == 1 and N == 2:
                print('No Profit',end='')
                break
            
            elif i-start >1 :
                print('(',end='')
                print(start ,j,end ='')
                print(')',end = ' ')
        print(end='\n')
            
