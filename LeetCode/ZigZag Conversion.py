'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a
fixed font for better legibility)
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:
string convert(string s, int numRows);
'''
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 :
            return s
        
        length = len(s)
        l = ['' for _ in range(length)]
        row = 0
        down = True
        
        for i in range(length):
            l[row] += s[i]
            if row == 0: down = True
            elif row == numRows-1: down = False
            
            if down : row += 1  #for moving down
            else: row -= 1      #for moving up
        
        return ''.join(l)
            
            
