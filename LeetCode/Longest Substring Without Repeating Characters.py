'''
Given a string, find the length of the longest substring without repeating characters.
'''

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        MAX = 0
        for i in range(len(s)):
            S = set()
            j = i
            while j < len(s):
                if s[j] not in S:
                    S.add(s[j])
                    MAX = max(len(S),MAX)
                    j+=1
                    if j == len(s): return MAX
                else:
                    MAX = max(len(S),MAX)
                    break
        
        return MAX
