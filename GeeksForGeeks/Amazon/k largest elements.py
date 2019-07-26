'''
Given an array of N positive integers, print k largest elements from the array.  The output elements should be printed in decreasing order.
'''

if __name__ == '__main__':
    
    t = int(input())
    for _ in range(t):
        
        n , k = map(int,input().split())
        A = list(map(int,input().split()))
        A.sort(reverse = True)
        print(*A[:k])
