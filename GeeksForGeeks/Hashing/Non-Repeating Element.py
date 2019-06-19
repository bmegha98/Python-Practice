'''
Find the first non-repeating element in a given array A of N integers.Array consists of only positive and negative integers and not zero.
For each testcase, print the required answer. If no such element exists, then print 0.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        ch = 0
        for i in range(N-1):
            if A[i] not in A[i+1:]:
                ch = A[i]
                break
        print(ch)
