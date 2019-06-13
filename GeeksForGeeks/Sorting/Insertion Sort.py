'''
The task is to complete insert() function which is used to implement Insertion Sort.
'''
def insert(arr):
    n = len(arr)
    for i in range(1,n):
        temp = arr[i]
        j = i
        while j > 0 and  (arr[j-1]> temp):
            arr[j] = arr[j-1]
            j-=1
        arr[j] = temp
        
    return arr
    
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        insert(arr)
        for i in range(n):
            print(arr[i],end=" ")
        print()
