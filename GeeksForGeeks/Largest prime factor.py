'''
Given a number N, the task is to find the largest prime factor of that number.
'''
def Prime(N):
    flag=0
    for i in range(2,int(pow(N,1/2))+1):
        if N%i==0:
            flag=1
            break
    if flag==0:return True
    else:return False
    
def Factors(N):
    l=[]
    for i in range(1,int(pow(N,1/2))+1):
        if N%i==0:
            l.append(i)
            l.append(N//i)
    return l
            
            
if __name__=='__main__':
    T=int(input())
    for i in range(T):
        N=int(input())
        l=Factors(N)
        for i in range(len(l)-1,-1,-1):
            if Prime(l[i]):
                print(l[i])
                break
