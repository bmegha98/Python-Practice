'''
Given N, count all ‘a’(>=1) and ‘b’(>=0) that satisfy the condition a3 + b3 = N.
'''
if __name__=='__main__':
    T=int(input())
    for i in range(T):
        count=0
        N=int(input())
        upper=int(pow(N,1/3))+1
        for j in range(1,upper+1):
            for k in range(upper,-1,-1):
                a=int(j**3)
                b=int(k**3)
                c=a+b
                if c==N:count+=1
    
        print(count)
