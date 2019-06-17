'''
Given an array of N integers. The task is to find the first element that occurs K number of times. If no element occurs K times then
print -1.
'''
from collections import OrderedDict
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        l = list(map(int,input().split()))
        N ,K = l[0],l[1]
        A = list(map(int,input().split()))
        d = OrderedDict()
        res = -1
        for ch in A :
            if ch not in d:d[ch]=1
            else:d[ch]+=1
        for k,v in d.items():
            if v == K:
                res = k
                break
        print(res)
        
