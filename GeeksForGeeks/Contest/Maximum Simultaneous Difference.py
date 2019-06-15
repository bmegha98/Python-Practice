'''
Given an unsorted array, find the maximum difference between its two consecutive elements in its sorted form.
Note : O(n) solution is expected.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        A.sort()
        diff = []
        for i in range(N-1):
            diff.append(A[i+1]-A[i])
        diff.sort(reverse = True)
        print(diff[0])
