from itertools import product
import math
def Prime(n):
    flag=0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            flag=1
            break
    if flag==0:return True
    else:return False
def PrimeNumbers(N):
    l=[]
    for i in range(2,N+1):
        if Prime(i)==True:l.append(i)
    return l
        
if __name__=='__main__':
    T=int(input())
    for i in range(T):
        N=int(input())
        p=PrimeNumbers(N)
        #print(p)
        pairs=list(product(p,repeat=2))
        #print(pairs)
        for j in range(len(pairs)):
            if pairs[j][0]*pairs[j][1]<=N:
                print(pairs[j][0],pairs[j][1],end=' ')
        print('')
