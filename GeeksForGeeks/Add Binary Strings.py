'''
Given two binary strings s1 and s2. Print the resultant string after adding given two binary strings.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        strings = list(input().split())
        s1 , s2 = strings[0],strings[1]
        m = 0
        
        if len(s1)<len(s2):
            zer = '0'*(len(s2)-len(s1))
            s1 = zer+s1
            m = len(s2)
        elif len(s2)<len(s1):
            zer = '0'*(len(s1)-len(s2))
            s2 = zer+s2
            m = len(s1)
      
        num1 = int(s1,2)
        num2 = int(s2,2)
        s = bin(num1+num2)
        s = s[2:]
        if len(s)!=m:
            zer = '0'*(m-len(s))
            s = zer+s
            
        print(s)
