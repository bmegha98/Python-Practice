'''
Given a string str containing alphanumeric characters, calculate sum of all numbers present in the string.
'''
if __name__ == '__main__':
    
    t = int(input())
    while t>0:
        
        s = input()
        res = 0
        i = 0
        
        while i <len(s):
            
            if s[i].isalpha():
                i += 1
            else :
                j = i
                num = ''
                while j < len(s) and s[j].isdigit():
                    num += s[j]
                    j += 1
            
                if num != '':
                    res += int(num)
                i = j
        
        print(res)
               
        t -= 1
