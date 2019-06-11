'''
The task is to complete bubble function which is used to implement Bubble Sort!
'''

def bubble(arr, i, n):
    for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
    
def bubbleSort(arr, n):
    for i in range(n-1):
        arr = bubble(arr, i, n)
    return arr
    
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        arr = bubbleSort(arr, n)
        print(*arr)
