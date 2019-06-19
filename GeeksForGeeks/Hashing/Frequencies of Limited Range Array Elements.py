'''
Given an array A[] of N positive integers which can contain integers from 1 to N where elements can be repeated or can be absent from the 
array. Your task is to count frequency of all elements from 1 to N.

Note: Expected time complexity is O(n) with O(1) extra space.
For each test case, output N space-separated integers denoting the frequency of each element from 1 to N.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        for i in range(N):
            A[i]-=1
        for i in range(N):
            A[A[i]%N]+=N
        for i in range(N):
            A[i]//=N
        print(*A)
