'''
Given N students with marks obtained by them in an exam. The task is to count the students with same name and marks.
For each testcase, print students name, marks and count of same student with same name and marks, all seperated by space. 
The output is sorted in lexigraphically sorted order of names and if two names are same then those are sorted in decreasing order of marks.
'''

from collections import OrderedDict
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        l = []
        N = int(input())
        d = OrderedDict()
        for i in range(N):
            lst = list(input().split())
            l.append((lst[0],int(lst[1])))
        l = sorted(l,key = lambda x:x[1],reverse = True)
        #print(l)
        for ch in l:
            if ch not in d : d[ch]=1
            else : d[ch]+=1
        
        #print(d)
        d= sorted(d.items(),key = lambda x :x[0][0])
        for ch in d:
            print(ch[0][0],ch[0][1],ch[1])
