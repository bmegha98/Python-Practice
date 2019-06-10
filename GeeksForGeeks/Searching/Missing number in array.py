'''
Given an array C of size N-1 and given that there are numbers from 1 to N with one element missing, the missing number is to be found.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        C = list(map(int,input().split()))
        actsum = sum(C)
        sumNat = (N*(N+1))//2
        print(sumNat-actsum)
