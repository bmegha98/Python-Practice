'''
Given two strings S1 and S2 as input, the task is to merge them alternatively i.e. the first character of S1 then the first character of 
S2 and so on till the strings end.

NOTE: Add the whole string if other string is empty.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        strings = list(input().split())
        s1 , s2 = strings[0] , strings[1]
        n1 , n2 = len(s1) , len(s2)
        a ,b= 0, 0
        res = []
        while a<n1 and b<n2 :
            res.append(s1[a])
            a+=1
            res.append(s2[b])
            b+=1
        
        while a<n1:
            res.append(s1[a])
            a+=1
        while b<n2:
            res.append(s2[b])
            b+=1
        
        print(''.join(res))
