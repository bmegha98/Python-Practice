'''
Given an array A of N integers and a number K. The task is to find the K-th largest element in the array.
For each testcase, print the K-th largest element, if exists, else print "-1" 
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        K = int(input())
        A.sort(reverse = True)
        try:
            print(A[K-1])
        except :
            print(-1)
