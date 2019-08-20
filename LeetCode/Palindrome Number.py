'''
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
'''
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if x == x[::-1]:return True
        return False
        
