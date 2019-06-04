'''
Given a string S, Check if characters of the given string can be rearranged to form a palindrome. 
For each testcase, in a new line, print "Yes" if is possible to make it a palindrome, else "No".
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        S = input()
        check = set(S)
        d = dict()
        for ch in S:
            if ch not in d:
                d[ch]=1
            else:
                d[ch]+=1
        
        even_count = len(list(filter(lambda x : x%2==0,d.values())))
        odd_count = len(list(filter(lambda x : x%2!=0,d.values())))
        
        if even_count == len(check) or odd_count == 1 :
            print('Yes')
        else :
            print('No')
