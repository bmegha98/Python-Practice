from collections import defaultdict
if __name__=='__main__':
    dfd=defaultdict(lambda:-1)
    n,m=map(int,input().split())
    for i in range(1,n+1):
        A=input()
        dfd[A]=dfd[A]+' '+str(i) if A in dfd else str(i)
    #print(dict(dfd))
   
    for i in range(m):
        B=input()
        print(dfd[B])
