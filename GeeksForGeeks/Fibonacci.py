'''
Tell only last two digits of the Nth number of Fibonacci series.
A better solution is to use the fact that after 300-th Fibonacci number last two digits starts repeating.
1) Find m = n % 300.
2) Return m-th Fibonacci number.
'''
def Fibonacci():
    f=[0,1]
    for i in range(2,300):
        f.append((f[i-1]+f[i-2])%100)
    return f

def PrintLastTwo(f,N):
    return f[N%300]
    
    
if __name__=='__main__':
    T=int(input())
    for i in range(T):
        N=int(input())
        f=Fibonacci()
        print(PrintLastTwo(f,N))
            
