'''
Your are celebrating vacation at your home and a task is given to you. You are given a number N and the task is to count ways to get N by
adding only given 3 integers 1, 2 and 3.

To reach 4th stair , count ways to reach 3rd stair ,2nd stair and 1st stair.
f(n) = f(n-3)+f(n-2)+f(n-1)
E.g : n = 1   n = 2              n = 3                   n = 4
        1      1->1             1->1->1               ==> (n=3)+(n=2)+(n=1)  = 4 + 2 + 1 = 7
                 2 (n = 0)        2->1
     
                                   1->2 ( n = 1)
                                    3   ( n= 0)

'''

def countWays(n) : 
    res = [0] * (n + 1) 
    
    if n < 2 : return 1
    res[0] = 1
    res[1] = 1
    res[2] = 2
    
    if n <3 : return res[n]
      
    for i in range(3, n + 1) : 
        res[i] = res[i - 1] + res[i - 2] + res[i - 3] 
      
    return res[n] 
    
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(countWays(N))
        
