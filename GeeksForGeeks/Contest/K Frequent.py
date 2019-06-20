'''
Given an array A of N integers and a number K. The task is to print the numbers with K frequency.
For each testcase, output the array elements in sorted order which are occurring K times in the array if present, else print -1.
'''
from collections import OrderedDict
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        num = list(map(int,input().split()))
        N , K = num[0],num[1]
        A = sorted(list(map(int,input().split())))
        d = OrderedDict()
        for ch in A :
            if ch not in d:d[ch]=1
            else:d[ch]+=1
        l = []
        for k,v in d.items():
            if v==K:l.append(k)
        if l==[]:print(-1)
        else:print(*l)
