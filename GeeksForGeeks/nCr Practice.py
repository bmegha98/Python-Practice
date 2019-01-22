def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
    
if __name__=='__main__':
    T=int(input())
    for i in range(T):
        l=list(map(int,input().split()))
        n,r=l[0],l[1]
        if n<r:print('0')
        else:
            tmp1=factorial(r)
            tmp2=factorial(n-r)
            tmp3=factorial(n)
            res=tmp3//(tmp1*tmp2)
            m = 1000000007
            print(res%m)
