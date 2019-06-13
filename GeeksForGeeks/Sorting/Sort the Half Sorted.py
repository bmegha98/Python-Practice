'''
Given an integer array of which both first half and second half are sorted. The task is to merge two sorted halves of the array into a 
single sorted array.
Print the sorted array with space separated values.
'''
def MergeSort(A,B):
    n1 , n2 = len(A),len(B)
    a , b = 0 , 0
    C = []
    while a < n1 and b < n2:
        if A[a]<B[b]:
            C.append(A[a])
            a+=1
        elif A[a]>B[b]:
            C.append(B[b])
            b+=1
        else :
            C.append(A[a])
            C.append(B[b])
            a+=1
            b+=1
    
    while a<n1: 
        C.append(A[a])
        a+=1
    
    while b<n2:
        C.append(B[b])
        b+=1
        
    print(*C)
    
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        A = list(map(int,input().split()))
        ind = -1
        for i in range(n-1):
            if A[i]>A[i+1]:
                ind = i
                break
        if ind!=-1:
            array1 = A[:ind+1]
            array2 = A[ind+1:]
            MergeSort(array1,array2)
        else:
            print(*A)
