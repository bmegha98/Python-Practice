'''
Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are anagram of each other 
or not. An anagram of a string is another string that contains same characters, only the order of characters can be different. 
For example, “act” and “tac” are anagram of each other.
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        strings = list(input().split())
        s1 = list(strings[0])
        s2 = list(strings[1])
        s1.sort()
        s2.sort()
        
        if ''.join(s1) == ''.join(s2):
            print('YES')
        else:
            print('NO')
        
