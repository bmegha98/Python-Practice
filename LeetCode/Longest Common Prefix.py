'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ''
        if not strs: return prefix
        strs.sort(key = len)
        tmp = strs[0]
        
        for i in range(len(tmp)):
            l = []
            for j in range(1,len(strs)):
                if tmp[i] == strs[j][i]:
                    l.append(True)
                else:l.append(False)
            if all(l):
                prefix += tmp[i]
            else:break
        
        return prefix
