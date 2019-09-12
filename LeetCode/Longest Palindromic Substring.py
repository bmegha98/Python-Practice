'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
'''

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
'''
def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        maxlen = 1
        low , high = 0 , 0
        start = 0
        for i in range(1,n):
            #even length
            low = i-1
            high = i
            while low >=0 and high <n and s[low] == s[high]:
                if high-low+1 > maxlen:
                    start = low
                    maxlen = high-low+1
                low -= 1
                high += 1
            #odd length
            low = i-1
            high = i+1
            while low >=0 and high <n and s[low] == s[high]:
                if high-low+1 > maxlen:
                    start = low
                    maxlen = high-low+1
                low -= 1
                high += 1
        return s[start:start+maxlen]
            



        
