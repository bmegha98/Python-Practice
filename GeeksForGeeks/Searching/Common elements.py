'''
Given three increasingly sorted arrays A, B, C of sizes N1, N2, and N3 respectively, you need to print all common elements in these arrays.

Note: Please avoid printing the same common element more than once.
For each testcase, print the common elements of array. If not possible then print -1.
'''


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        sizes = list(map(int,input().split()))
        N1 ,N2 ,N3 = sizes[0] , sizes[1] , sizes[2]
        A = set(list(map(int,input().split())))
        B = set(list(map(int,input().split())))
        C = set(list(map(int,input().split())))
        tmp = A.intersection(B)
        final = sorted(tmp.intersection(C))
        if final == [] :print(-1)
        else : print(*final)
        
        
