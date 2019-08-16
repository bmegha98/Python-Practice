'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s or len(s) <= 1 : return s
        size = len(s)
        while size > 0 :
            for i in range(len(s)-(size - 1)):
                res = s[i : size+i]
                if res == res[::-1]:
                    return res
            size -= 1
        return ''
        
