'''
For an integer n find number of trailing zeroes in n! . 
'''
import math
if __name__=='__main__':
    T=int(input())
    for i in range(T):
        N=int(input())
        tmp=math.floor(N/5)
        sum=tmp
        while tmp>=5:
            tmp=math.floor(tmp/5)
            sum+=tmp
            
        print(sum)
