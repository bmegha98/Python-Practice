'''
Given n Magnets which are placed linearly, with each magnet to be considered as of point object. Each magnet suffers force from 
its left sided magnets such that they repel it to the right and vice versa. All forces are repulsive. The force being equal to the 
distance (1/d , d being the distance). Now given the positions of the magnets, the task to find all the points along the linear line 
where net force is ZERO. 

Note: Distance have to be calculated with precision of 0.0000000000001.

'''
def Search(low,high,arr,n):
    f = 0.0
    m = (low+high)/2
    for i in range(0,n):
        x = 1/(m-arr[i])
        f+= x
        
    if abs(f)< 0.0000000000001 :
        return m
    if f < 0:
        return Search(low,m,arr,n)
    else :
        return Search(m,high,arr,n)
        
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        M = list(map(int,input().split()))
        for i in range(0,N-1):
            pos = Search(M[i],M[i+1],M,N)
            print("{:.2f}".format(pos),end=' ')
        print(end='\n')
