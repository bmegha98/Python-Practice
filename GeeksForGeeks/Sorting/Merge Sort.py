'''
The task is to complete merge() function which is used to implement Merge Sort.
'''

def mergeSort(arr):
    n = len(arr)
    if n>1:
        n1 = n//2
        n2 = n-n1
        L = arr[:n1]
        R = arr[n1:]
        mergeSort(L)
        mergeSort(R)
        
        a , b ,c = 0 , 0, 0
        
        while a < len(L) and b < len(R):
            if L[a] < R[b]:
                arr[c]=L[a]
                a+=1
                c+=1
            else:
                arr[c] = R[b]
                b+=1
                c+=1
    
        while a<len(L): 
            arr[c] = L[a]
            a+=1
            c+=1
    
        while b<len(R):
            arr[c] = R[b]
            b+=1
            c+=1
            
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        mergeSort(arr)
        for i in range(n):
            print(arr[i],end=" ")
        print()
    
