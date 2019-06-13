'''
Given a sorted binary array A of N elements. The task is to find the index from where 0 ends in the given array.
For each testcase, print the index (0-based) where 0 ends. Print "-1" (without quotes) if 0 is not present.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        pos = -1
        try:
            pos = len(A)-A[::-1].index(0)-1
        except :
            pos = -1
        print(pos)
