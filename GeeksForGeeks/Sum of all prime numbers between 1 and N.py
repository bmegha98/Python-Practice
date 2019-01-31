'''
Given a positive integer N, calculate the sum of all prime numbers between 1 and N(inclusive).
'''
def SumOfPrimes(N):
    prime=[True]*(N+1)
    prime[0]=prime[1]=False
    p=2
    while p*p<=N:
        if prime[p]==True:
            for i in range(p*p,N+1,p):
                prime[i]=False
        p+=1
    sum=0
    for i in range(2,N+1):
        if prime[i]:sum+=i
    return sum
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        print(SumOfPrimes(N))
