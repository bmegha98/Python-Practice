'''
Given an array with positive number the task to find the largest subsequence from array that contain elements which are Fibonacci numbers.
'''
def Fib(N):
    a , b = 0 ,1
    res = [a]
    for i in range(N):
        a , b = b,a+b
        res.append(a)
    return res

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        A = list(map(int,input().split()))
        res = Fib(max(A))
        for ch in A:
            if ch in res:print(ch,end=' ')
        print(end='\n')
        
