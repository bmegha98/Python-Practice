'''
Given an array C[], write a program that prints 1 if array is sorted in non-decreasing order, else prints 0.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        tmp = [x for x in A]
        tmp.sort()
        if tmp == A:print(1)
        else : print(0)
