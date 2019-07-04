'''
Below is a function given to you. The task is to find the value of function for given number X.
Function : f(X) = f(X+1) + X; f(0) = 1.
'''

def Function(X):
    if X == 0: return 1
    return Function(X-1)-X
    
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        X = int(input())
        n = Function(X)
        print(n+X)
        
