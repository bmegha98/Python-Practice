'''
Given a number N. Find a number K such that product of digits of K must be equal to N.
Note : K must be as small as possible.
'''
def SmallestNumber(n):
    if n>=0 and n<=9:
        return n
    l=[]
    for i in range(9,1,-1):
        while n%i==0:
            l.append(i)
            n=n//i
    if n!=1:
        return -1
    k=0
    while len(l)!=0:
        k=k*10+l[-1]
        l.pop()
    return k
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        print(SmallestNumber(N))
