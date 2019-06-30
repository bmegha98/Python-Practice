'''
Given the total number of persons n and a number k which indicates that k-1 persons are skipped and kth person is killed in circle in a 
fixed direction.The task is to choose the safe place in the circle so that when you perform these operations starting from 1st place in the
circle, you are the last one remaining and survive.
'''
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        nk=[int(x) for x in input().strip().split()]
        n=nk[0]
        k=nk[1]
        
        print(josephus(n,k))
        
        T-=1
if __name__=="__main__":
    main()
    
def josephus(n,k):
    '''
    # Recursive
    if n==1:return 1
    return (josephus(n-1,k)+k-1)%n +1
    '''
    
    '''
    # Iterative 1
    sum = 0
    for i in range(2,n+1):
        sum = (sum+k)%i
    return sum+1
    '''
    # Iterative 2
    
    A = [i for i in range(1,n+1)]
    size = n
    i = 0
    while size!=1:
        rem = (i+k-1)%size
        i = rem
        del A[rem]
        size-=1
    return A[0]
