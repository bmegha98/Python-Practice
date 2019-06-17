'''
Given a N x N matrix. Write a program to find count of all the distinct elements common to all rows of the matrix. 
Print count of such elements.
'''
from collections import OrderedDict
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        M = list(map(int,input().split()))
        d = OrderedDict()
        count = 0
        for i in range(N):
            for j in range(N):
                if i == 0:
                    d[M[i*N+j]] = 1
                    continue
                if M[i*N+j] in d and d[M[i*N+j]] == i:
                    d[M[i*N+j]] += 1
                    
        for i in d:
            if d[i]==N:count+=1
        print(count)
