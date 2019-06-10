'''
Monu lives in a society which is having high rise buildings. This is the time of sunrise and monu wants see the buildings receiving the 
sunlight. Help him in counting the number of buildings recieving the sunlight.
Given an array H representing heights of buildings. You have to count the buildings which will see the sunrise
(Assume : Sun rise on the side of array starting point).
'''

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        N = int(input())
        buildings = list(map(int,input().split()))
        count = 1
        l = [buildings[0]]
        for i in range(1,N):
            if buildings[i] > l[-1]:
                l.append(buildings[i])
                count+=1
        
        print(count)
    
