'''
Given an array A of N integers. The task is to count the pairs which are adjacent and equal.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        count = 0
        for i in range(N-1):
            if A[i]==A[i+1]:
                count+=1
        print(count)
