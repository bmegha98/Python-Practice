'''
Find the missing element from  an ordered array A[ ], consisting of N elements representing an Arithmetic Progression (AP) .
The series should have a missing element in between a perfect A.P. with no missing element will not be considered.
Output:
Print out the missing element. 
'''
import sys
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        if N == 2 :
            d = (A[1]-A[0])//2
        else :
            d = sys.maxsize
            for i in range(0,N-1):
                diff = A[i+1]-A[i]
                d = min(d,diff)
        
        AP = [A[0]]
        while True:
            term = AP[-1]+d
            if term not in A : 
                print(term)
                break
            AP.append(term)
