'''
Given a binary array A[] of size N. The task is to arrange array in increasing order.

Note: The binary array contains only 0  and 1.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        A.sort()
        print(*A)
