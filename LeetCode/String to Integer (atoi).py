'''
mplement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting
from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as
a numerical value.
The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior
of this function.
If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str 
is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

Only the space character ' ' is considered as whitespace character.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the
numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
'''

class Solution(object):
    def myAtoi(self, string):
        """
        :type str: str
        :rtype: int
        """
        if len(string) == 1 and not string.isdigit():return 0
        string = string.lstrip()
        if string == '' or (not(string[0].isdigit()) and string[0] not in ['+','-']) : return 0
        res = ''
        for ch in string:
            if ch.isdigit() or (res == '' and ch in ['+','-']):
                res += ch
            else:
                break
        
        if len(res) == 1 and not res.isdigit():return 0
        
        if res[0] in ['+','-']:
                if res[0] == '+': res = res[1:]
	        
        if int(res) > pow(2,31) - 1 : return pow(2,31) - 1
        elif int(res) < -pow(2,31) : return -pow(2,31)
        
        
        return int(res)
