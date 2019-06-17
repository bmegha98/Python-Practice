'''
Given two arrays A and B of positive integers. Your task is to find numbers which are present in the first array, but not present
in the second array.
'''
from collections import OrderedDict
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        sizes = list(map(int,input().split()))
        N , M = sizes[0],sizes[1]
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))
        d = OrderedDict()
        l = []
        for ch in B:
            if ch not in d:
                d[ch] = True
                
        for ch in A:
            if ch not in d: l .append(ch)
        print(*l)
