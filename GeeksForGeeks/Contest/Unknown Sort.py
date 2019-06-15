'''
You are given an array A of size N. You are also given an integer K. You need to sort the elements such that element that has the greater
remainder when divided by K comes first. If two numbers give the same remainder on division by K then the number that is greater comes 
first.
For each testcase, in a new line, print the sorted array.
'''
from collections import OrderedDict
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        K = int(input())
        d = OrderedDict()
        A.sort(reverse = True)
        repeated = [0]*(A[0]+1)
        #print(A)
        
        for ch in A :
            d[ch] = ch%K
            if repeated[ch] == 0 : repeated[ch] =1
            else : repeated[ch]+=1
        
        #print(d)
        #print(repeated)
        
        S = sorted(d.items(),key = lambda x : x[1],reverse = True)
        #print(S)
        for ch in S : 
            l = [str(ch[0]) for i in range(repeated[ch[0]])]
            print(' '.join(l),end = ' ')
        
        print(end='\n')
