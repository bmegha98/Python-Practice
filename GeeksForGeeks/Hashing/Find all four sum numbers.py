'''
Given an array A of size N, find all combination of four elements in the array whose sum is equal to a given value K. For example, if the
given array is {10, 2, 3, 4, 5, 9, 7, 8} and K = 23, one of the quadruple is “3 5 7 8” (3 + 5 + 7 + 8 = 23).
For each test case in a new line print all the quadruples present in the array separated by space which sums up to value of K.
Each quadruple is unique which are separated by a delimeter "$" and are in increasing order.
'''
def quickSort(arr,low,high):
    if low < high:
        pi = partition(arr,low,high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)

def partition(arr,low,high):
    pivot = arr[high]
    i = low-1
    for j in range(low,high):
        if arr[j]<pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1
    
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        num = list(map(int,input().split()))
        N , K = num[0],num[1]
        arr = list(map(int,input().split()))
        quickSort(arr,0,N-1)
        curr = ''
        lst = []
        for i in range(N-3):
            for j in range(i+1,N-2):
                for k in range(j+1,N-1):
                    for l in range(k+1,N):
                        if arr[i]+arr[j]+arr[k]+arr[l]== K:
                            curr = str(arr[i])+str(arr[j])+str(arr[k])+str(arr[l])
                            if curr not in lst:
                                lst.append(curr)
                                print(arr[i],arr[j],arr[k],arr[l],'$',end='')
                            
                            
        if lst == []:
            print(-1)
        else : 
            print(end = '\n')
