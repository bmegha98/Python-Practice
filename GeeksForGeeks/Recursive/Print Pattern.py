'''
Print a sequence of numbers starting with N, without using loop, in which  A[i+1] = A[i] - 5,  if  A[i]>0, else A[i+1]=A[i] + 5  repeat it 
until A[i]=N.
'''
# Recursive

def Sequence(N):
    if N>0:
        print(N,end=' ')
        Sequence(N-5)
    
    print(N,end=' ')
    
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        Sequence(N)
        print()
        
# Iterative

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        tmp = N
        while True:
            if tmp<=0:break
            print(tmp,end=' ')
            tmp-=5
        while tmp<=N:
            print(tmp,end=' ')
            tmp+=5
        print()
            
