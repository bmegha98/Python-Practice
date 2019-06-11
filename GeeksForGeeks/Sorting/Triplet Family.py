'''
Given an array A of integers. Find three numbers such that sum of two elements equals the third element and return the triplet in a 
container result, if no such triplet is found return the container as empty.
Your Task: Your task is to complete the function to find triplet and return container containing result.
'''
def findTriplet(arr,n):
    arr.sort()
    for i in range(n-2):
        for j in range(i+1,n-1):
            s = arr[i]+arr[j]
            if s in arr[j+1:]:
                return [arr[i],arr[j],s]
    return []
    
    if __name__=="__main__":
    t=int(input())
    for j in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        a=findTriplet(arr,n)
        if(len(a)==3):
            print(1)
        else:
            print(-1)
