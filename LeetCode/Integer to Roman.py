class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman = ''
        number = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        sym = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']
        i = 12
        while num > 0:
            rem = num // number[i]
            num = num % number[i]
            for j in range(rem):
                roman += sym[i]
                
            i -= 1
        return roman
