'''
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
'''
phone = {'2': 'abc','3': 'def','4': 'ghi','5': 'jkl','6': 'mno','7': 'pqrs','8': 'tuv','9': 'wxyz'}
def PhoneCombination(digits,s,temp):
    if digits == []:
        temp.append(s)
        return
    for ch in phone[digits[0]]:
        PhoneCombination(digits[1:],s+ch,temp)
    
    return temp
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        s = ''
        l = []
        digits = list(digits)
        return PhoneCombination(digits,s,l)
        
