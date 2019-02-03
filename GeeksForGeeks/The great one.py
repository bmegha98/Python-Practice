'''
Given an array A of size N which consists of positive integers. The task is to make the largest number K from array elements 
such that every chosen array element has exactly 3 divisiors. If no such number can be formed then print -1.
'''
from math import sqrt
from itertools import permutations
def largest(l): 
    lst = [] 
    for i in permutations(l, len(l)): 
        lst.append("".join(map(str,i)))  
    return max(lst) 
def isPrime(n): 
    if (n <= 1): 
        return False
    if (n <= 3): 
        return True
    if (n % 2 == 0 or n % 3 == 0): 
        return False
      
    k= int(sqrt(n))+1
    for i in range(5,k,6): 
        if (n % i == 0 or n % (i + 2) == 0): 
            return False
  
    return True
 
def isThreeDisctFactors(n): 
    sq = int(sqrt(n)) 
    if (1 * sq * sq != n): 
        return False
    if (isPrime(sq)): 
        return True
    else: 
        return False
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        Array=list(map(int,input().split()))
        l=[]
        for el in Array:
            if isThreeDisctFactors(el):
                l.append(el)
        if len(l)==0:
            print('-1')
        else:
            print(largest(l))
                
