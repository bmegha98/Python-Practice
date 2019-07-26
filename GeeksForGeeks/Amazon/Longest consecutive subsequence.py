'''
Given an array arr[] of positive integers. Find the length of the longest sub-sequence such that elements in the subsequence are 
consecutive integers, the consecutive numbers can be in any order.
'''
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        A = list(map(int,input().split()))
        A.sort()
        M = 1
        count = 1
        for i in range(n-1):
            if A[i]+1 == A[i+1]:
                count += 1
                if M < count:
                    M = count
            else:
                count = 1
        print(M)
        
