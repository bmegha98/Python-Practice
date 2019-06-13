'''
Given an array A[] of integers, sort the array according to frequency of elements. That is elements that have higher frequency come first.
If frequencies of two elements are same, then smaller number comes first.
'''

from collections import OrderedDict 
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = sorted(list(map(int,input().split())))
        d = OrderedDict()
        for ch in A :
            if ch not in d:
                d[ch] =1
            else :
                d[ch]+=1
        #print(d)
        new_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
        #print(new_d)
        
        for i in new_d:
                l = [str(i[0]) for x in range(i[1])]
                print(' '.join(l),end = ' ')
        
        print(end = '\n')
