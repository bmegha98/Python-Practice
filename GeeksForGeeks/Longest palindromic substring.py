'''
Given a string, find the longest substring which is palindrome.
'''
def substrings(s):
    l = len(s)
    for i in range(l, 0, -1):
        for j in range(l-i+1):
            yield s[j: j+i]
            
def palindrome(s):
    return s == s[::-1]
    
def findLongestPalindromicString(seq):
    for l in substrings(seq):
        if palindrome(l):
            print(l)
            break
