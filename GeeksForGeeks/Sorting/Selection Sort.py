'''
The task is to complete select() function which is used to implement Selection Sort.
'''
def select(arr):
    for i in range(n-1):
        ind = i
        for j in range(i+1,n):
            if arr[j]<arr[ind]:
                ind = j
        arr[i],arr[ind] = arr[ind],arr[i]
    return arr
    
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        select(arr)
        for i in range(n):
            print(arr[i],end=" ")
        print()
