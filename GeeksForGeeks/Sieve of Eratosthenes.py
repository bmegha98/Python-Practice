'''
Given a number N, calculate the prime numbers upto N using Sieve of Eratosthenes.  
'''
def PrintPrime(N):
    l=[]
    prime=[True for i in range(N+1)]
    p=2
    while p*p<=N:
        if prime[p]:
            for i in range(p*p,N+1,p):
                prime[i]=False
        p+=1
    for i in range(2,N+1):
        if prime[i]==True:
            l.append(i)
    print(' '.join(str(i) for i in l))
            
        

if __name__=='__main__':
    T=int(input())
    for i in range(T):
        N=int(input())
        PrintPrime(N)
