'''
Given a string S consisting of lowercase Latin Letters. Find the first non repeating character in S.
'''
'''
// TLE
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        s = input()
        res = -1
        tmp = s
        i = 0
        while len(tmp)>0:
            ch = tmp[i]
            if ch not in tmp[i+1:]:
                res = ch
                break
            else :
                tmp= [x for x in tmp if x!=ch]
        print(res)
'''
from collections import OrderedDict
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        s = input()
        d = OrderedDict()
        res = -1
        for i in s :
            if i not in d:
                d[i]=1
            else :
                d[i]+=1
        
        for i in d:
            if d[i]==1:
                res = i
                break
        print(res)
