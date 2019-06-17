'''
Given two arrays A and B of equal size N, the task is to find if given arrays are equal or not. Two arrays are said to be equal if both of
them contain same set of elements, arrangements (or permutation) of elements may be different though.
Note : If there are repetitions, then counts of repeated elements must also be same for two array to be equal.
For each test case, print 1 if the arrays are equal else print 0.
'''
from collections import OrderedDict
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))
        d = OrderedDict()
        flag = 1
        for ch in A :
            if ch not in d : d[ch] = 1
            else : d[ch]+=1
       
        #print(d)
        for ch in B :
            if ch in d:d[ch]-=1
            else:
                flag = 0
                break
        #print(d)
        if flag:
            if all(x==0 for x in d.values()) : flag = 1
            else : flag = 0
        print(flag)
