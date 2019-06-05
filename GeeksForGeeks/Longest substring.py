'''
Given a string S, find length of the longest substring with all distinct characters.  
For example, for input "abca", the output is 3 as "abc" is the longest substring with all distinct characters.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        s = input()
        tmp =[]
        i =0
        while i<len(s):
           
            string = s[i]
            for j in range(i+1,len(s)):
                if s[j] not in string:
                    string+=s[j]
                else :
                    break
            tmp.append(string)
            i+=1
        #tmp.append(string)
        #print(*tmp)
        maxlen = len(tmp[0])
        
        for ch in tmp:
            if len(ch)> maxlen:
                maxlen = len(ch)
               
        
        print(maxlen)
