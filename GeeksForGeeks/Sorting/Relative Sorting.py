'''
Given two arrays A1[] and A2[] of size N and M respectively. The task is to sort A1 in such a way that the relative order among the 
elements will be same as those in A2. For the elements not present in A2, append them at last in sorted order. It is also given that the 
number of elements in A2[] are smaller than or equal to number of elements in A1[] and A2[] has all distinct elements.

Note: Expected time complexity is O(N log(N)).
'''

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        sizes = list(map(int,input().split()))
        A1 = list(input().split())
        A2 = list(input().split())
        N , M = sizes[0] , sizes[1]
        d = dict()
        for ch in A1:
            if ch not in d :
                d[ch] = 1
            else :
                d[ch]+=1
        #print(d)
        
        for ch in A2:
            if ch in d:
                l = [ch for i in range(d[ch])]
                print(' '.join(l),end = ' ')
                del d[ch]
        #print(d)
        
        if d!= {}:
            for i in sorted(d.keys(),key = int):
                l = [i for x in range(d[i])]
                print(' '.join(l),end = ' ')
        
        print(end='\n')
