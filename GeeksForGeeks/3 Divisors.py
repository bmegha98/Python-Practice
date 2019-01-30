'''
Given a value N, you need to find how many numbers less than or equal to N have numbers of divisors exactly equal to 3.
'''
'''
//TLE
from math import sqrt
def NumDivisors(n):
    c=0
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            if n/i==i:c+=1
            else:c+=2
    return c

if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        count=0
        N=int(input())
        for i in range(N+1):
            if NumDivisors(i)==3:count+=1
        print(count)
                
'''
// 3 divisors=1,sqrt(p),p --> squares of prime numbers
def numbersWith3Divisors(n):  
    prime=[True]*(n+1) 
    prime[0] = prime[1] = False 
    p=2
    while (p*p<=n): 
        if (prime[p] == True): 
            for i in range(p*2,n+1,p): 
                prime[i] = False 
        p+=1 
    i,c=0,0
    while (i*i <= n):  
        if (prime[i]): 
            c+=1 
        i+=1
    return c

if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        n=int(input())
        print(numbersWith3Divisors(n))
        
