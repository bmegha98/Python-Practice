'''
Given an array of names (consisting of lowercase characters) of candidates in an election. A candidate name in array represents a vote 
casted to the candidate. Print the name of candidate that received Max votes. If there is tie, print lexicographically smaller name.

For each testcase, print the name of the candidate with the maximum votes, and also print the votes casted for the candidate. The name 
and votes are separated by a space.
'''
from collections import OrderedDict
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = sorted(list(input().split()))
        d = OrderedDict()
        for ch in A:
            if ch not in d:d[ch]=1
            else : d[ch]+=1
        l = sorted(d.items(),key = lambda x:x[1],reverse = True)
        print(l[0][0],l[0][1])
