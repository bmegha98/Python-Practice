'''
Given a number N, check if a number is perfect or not. A number is said to be perfect if sum of all its factors excluding the number
itself is equal to the number.
'''
import math
if __name__=='__main__':
    T=int(input())
    for i in range(T):
        N=int(input())
        sum=0
        for j in range(1,int(math.sqrt(N))+1):
            if N%j==0:
                sum+=j
                sum+=(N//j)
        if sum==N:print('1')
        else:print('0')
