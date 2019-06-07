'''
Given a string S. The task is to find the longest substring such that characters in the substrings are of the form abcdefgh...xyzabcd... 
The two adjacent characters should have difference of 1 and the next character should be lexiographically greater than the previous 
character. However, z can be followed by a, despite a not being lexiograpghically greater.
If there are multiple answers then print the first such string.

For each testcase, in a new line, print the longest substring and length in separate lines.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        l = []
        final = []
       
        for i in range(len(S)):
            if l ==[]:l.append(S[i])
            elif (ord(S[i])-ord(l[-1]))==1 or ( S[i]=='a' and l[-1]=='z'):
                l.append(S[i])
            else:
                
                string = ''.join(l)
                final.append(string)
                l=[]
                l.append(S[i])
        
        if l !=[]:final.append(''.join(l))
        
        final.sort(key = len,reverse = True)
                
        
        print(final[0])
        print(len(final[0]))
    
