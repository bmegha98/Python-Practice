'''
Given a 32-bit signed integer, reverse digits of an integer.
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the
purpose of this problem,assume that your function returns 0 when the reversed integer overflows.
'''
'''
In C++:

class Solution {
public:
    int reverse(int x) 
    {
        long long int ans = 0;
        while(x!=0)
        {
            ans = (ans*10) + (x %10);
            x = x/10;
            if(ans > INT_MAX)
                return 0;
            if(ans < INT_MIN)
                return 0;
        }
        return ans;
    }
};
'''
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:return x
        x = str(x)
        res = ''
        if x[0] == '-':
            res += ''.join(x[:0:-1])
            res = res.lstrip('0')
            res = '-'+res
        else:
            res += ''.join(x[::-1])
            res = res.lstrip('0')
         
        if int(res) < -pow(2,31) or int(res) > pow(2,31)-1 : return 0
        return int(res)
    
