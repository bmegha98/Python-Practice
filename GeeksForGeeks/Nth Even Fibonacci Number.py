'''
Given a positive integer N, find the Nth Even Fibonacci number. Since the answer can be very large, print the answer modulo 1000000007.
'''
'''
//TLE
def fibonacci(n):
    if n==1:return 1
    if n==2:return 1
    return fibonacci(n-1)+fibonacci(n-2)
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        print(fibonacci(N*3)%1000000007)
'''
if __name__=='__main__':
    T=int(input())
    fib=[0 for j in range(3001)]
    fib[1]=1
    fib[2]=1
    i=3
    while i<3001:
        fib[i]=fib[i-1]+fib[i-2]
        i+=1
    for _ in range(T):
        N=int(input())
        print(fib[N*3]%1000000007)
