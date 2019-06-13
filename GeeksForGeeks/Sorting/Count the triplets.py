'''
Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.
For each test case, print the count of all triplets, in new line. If no such triplets can form, print "-1".
'''
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = sorted(list(map(int,input().split())))
        count = 0
        for i in range(n-1,1,-1):
            l = 0
            r = i-1
            while l<r:
                if arr[l]+arr[r] == arr[i]:
                    count+=1
                    l+=1
                elif arr[l]+arr[r] < arr[i]:
                    l+=1
                else:
                    r-=1
        
        if count:print(count)
        else : print(-1)
