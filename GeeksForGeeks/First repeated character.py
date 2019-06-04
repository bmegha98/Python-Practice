'''
Given a string S. The task is to find the first repeated character in it. We need to find the character that occurs more than once and
whose index of first occurrence is smallest. S contains only lowercase letters.

//TLE

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        rep = -1
        index = len(S)
        for i in range(len(S)):
            temp = S[i+1:].find(S[i])
            if temp!= -1:
                if temp+i < index:
                    rep = S[i]
                    index = temp+i
            else:
                continue
        print(rep)
            
'''
def FirstRepeat(string):
    s = set()
    res = -1
    if len(string)==0:
        print(-1)
        return
    
    for ele in string:
        if ele in s :
            res = ele
            break
        else:
            s.add(ele)
    print(res)
            
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        FirstRepeat(S)
        
