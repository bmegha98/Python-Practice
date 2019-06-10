'''
Given an array A of N integers. The task is to find a peak element in it.
An array element is peak if it is not smaller than its neighbours. For corner elements, we need to consider only one neighbour.

Note: There may be multiple peak element possible, in that case you may return any valid index.
'''

def peakElement(arr, n):
    if n==1 : return 0
    for i in range(0,n):
        if i == 0 and arr[1]<arr[0]: return 0
        if i == (n-1) and arr[n-1]>arr[n-2]: return n-1
        else:
            if (arr[i-1]< arr[i])and(arr[i+1] < arr[i]):
                return i

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = peakElement(arr, n)
        flag = False
        if index == 0 and n==1:
            flag = True
        elif index==0 and arr[index]>arr[index+1]:
            flag = True
        elif index==n-1 and arr[index]>arr[index-1]:
            flag = True
        elif arr[index-1] < arr[index] and arr[index] > arr[index+1]:
            flag = True
        else:
            flag = False
        if flag:
            print(1)
        else:
            print(0)

