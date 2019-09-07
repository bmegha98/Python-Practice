class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
   
        sym = {'I': 1,'IV' : 4,'V' : 5,'IX' : 9,'X' : 10,'XL' : 40,'L' : 50,'XC' : 90,'C' : 100,'CD' : 400,'D' : 500,'CM' : 900,'M' : 1000}
        
        for i in range(len(s)):
            if i != len(s)-1:
                if sym[s[i]] >= sym[s[i+1]]:
                    num += sym[s[i]]
                else:
                    num -= sym[s[i]]
            else:
                num += sym[s[i]]
        
        return num
                    
