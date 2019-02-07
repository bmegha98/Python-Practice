'''
Given an array A[], Your task is to complete the function printDuplicates which prints the duplicate elements of the given array. 
If no duplicate element is found  print -1.
'''
def printDuplicates(arr,n):
    c = 1
    for i in range(n):
        ind = arr[i] % n
        arr[ind] += n

        if arr[ind]//n == 2:
            print(ind,end= " ")
            c = 0

    if c:print('-1')
