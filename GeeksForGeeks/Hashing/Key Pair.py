'''
Given an array A of N positive integers and another number X. Determine whether or not there exist two elements in A whose sum is exactly 
X.Print "Yes" if there exist two elements in A whose sum is exactly X, else "No" (without quotes).
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        num = list(map(int,input().split()))
        N , X = num[0],num[1]
        A = sorted(list(map(int,input().split())))
        low ,high = 0,N-1
        flag = 0
        while low<high:
            if A[low]+A[high] == X:
                flag = 1
                break
            elif A[low]+A[high]>X:
                high-=1
            else:
                low+=1
        if flag:print('Yes')
        else:print('No')
