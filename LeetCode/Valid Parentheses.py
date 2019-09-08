'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {'(' : 1 ,')' : 1,'{' : 3,'}': 3,'[' : 2 , ']': 2}
        if s == '':return True
        if len(s) % 2 != 0 : return False
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            elif s[i] == ')' or s[i] == ']' or s[i] == '}':
                if stack == [] or d[s[i]] != d[stack[-1]]: return False
                else:
                    stack.pop()
        if stack == [] : return True
        else : return False
