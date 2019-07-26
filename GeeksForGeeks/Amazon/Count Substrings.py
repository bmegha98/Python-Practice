'''
Given a binary string S. The task is to count the number of substrings that starts and end with 1. For example, if the input string is 
“00100101”, then there are three substrings “1001”, “100101” and “101”.
'''
if __name__ == '__main__':
    
    t = int(input())
    while t>0:
        s = input()
        
        x = s.count('1')
        res = (x * (x-1))//2
        print(res)
        '''
        res = 0
        for i in range(len(s)):
            if s[i] == '1':
                for j in range(i+1,len(s)):
                    if s[j] == '1':
                        res += 1
        print(res)
        '''
        t -= 1
