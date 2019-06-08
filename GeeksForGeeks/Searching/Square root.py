'''
Given an integer x. The task is to find the square root of x. If x is not a perfect square, then return floor(√x).
'''
'''
from math import sqrt
def floorSqrt(x): 
    return math.floor(sqrt(x))
    
'''
import math
def NPSquare(N): 
    nextN = math.floor(math.sqrt(N)) + 1
    return nextN * nextN 
    
def floorSqrt(x):
    low = 0
    high = x
    while low<=high:
        mid = (low+high)//2
        if (mid*mid == x) or ((mid+1)*(mid+1) == NPSquare(x)):
            return mid
        if (mid*mid) > x: high = mid-1
        else : low = mid+1
        
    return -1
