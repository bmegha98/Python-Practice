'''
Consider a long alley with a N number of doors on one side. All the doors are closed initially. You move to and fro in the alley 
changing the states of the doors as follows: you open a door that is already closed and you close a door that is already opened. 
You start at one end go on altering the state of the doors till you reach the other end and then you come back and start altering
the states of the doors again.

In the first go, you alter the states of doors numbered 1, 2, 3, … , n.

In the second go, you alter the states of doors numbered 2, 4, 6 …

In the third go, you alter the states of doors numbered 3, 6, 9 …

You continue this till the Nth go in which you alter the state of the door numbered N.

You have to find the number of open doors at the end of the procedure.
'''
'''
//TLE
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        doors=[0 for i in range(N+1)]
        for i in range(1,N+1):
            j=i
            while j<=N:
                if doors[j]==0:doors[j]=1
                else:doors[j]=0
                j+=i
        print(doors[1:].count(1))
'''
'''
Every door is visited by its factors and door is open if number of its factors are odd. Perfect square number has Odd number of factors.
'''
import math
if __name__=='__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        print(int(math.sqrt(N)))
        
