'''
Given two arrays: arr1[0..m-1] of size m and arr2[0..n-1] of size n. Task is to check whether arr2[] is a subset of arr1[] or not. Both 
the arrays can be both unsorted or sorted. It may be assumed that elements in both array are distinct.
Print "Yes"(without quotes) if arr2 is subset of arr1.
Print "No"(without quotes) if arr2 is not subset of arr1.
'''

from collections import OrderedDict
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        sizes = list(map(int,input().split()))
        N , M = sizes[0],sizes[1]
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))
        flag = 1
        if M<=N:
            d = OrderedDict()
            for ch in A:
                if ch not in d:d[ch]=True
            for ch in B:
                if ch not in d:
                    flag = 0
                    break
            if flag:print('Yes')
            else : print('No')
        else:print('No')
                
