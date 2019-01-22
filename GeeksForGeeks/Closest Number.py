'''
Given non-zero two integers N and M. The problem is to find the number closest to N and divisible by M. 
If there are more than one such number, then output the one having maximum absolute value.
'''
def Closest(N,M):
    M=abs(M)
    q=N//M
    n1= M*q
    n2=M*(q+1)
    
    diff1=N-n1
    diff2=n2-N
    
    if diff1>diff2:print(n2)
    elif diff2>diff1:print(n1)
    else:
        if abs(n1)>abs(n2):print(n1)
        else:print(n2)
       
if __name__=='__main__':
    T=int(input())
    for i in range(T):
        l=list(map(int,input().split()))
        N,M=l[0],l[1]
        Closest(N,M)
