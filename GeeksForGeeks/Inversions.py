'''
Count number of inversions in an array in O(log n) time.
'''
def Merge(A,l,m,h):
    inv_count = 0
    temp = [0]*len(A)
    i , j,k = l,m+1,l
    while i<=m and j<=h:
        if A[i]<= A[j]:
            temp[k] = A[i]
            i += 1
        else:
            temp[k] = A[j]
            inv_count += (m+1-i)
            j += 1
        k += 1
        
    
    while i<= m :
        temp[k] = A[i]
        i += 1
        k += 1
    
    while j<= h:
        temp[k] = A[j]
        k += 1
        j += 1
    
    for p in range(l,h+1):
        A[p] = temp[p]  
    
    return inv_count
def Mergesort(A , low , high):
    count = 0
    if low < high:
        mid = (low+high)//2
        count = Mergesort(A,low,mid)
        count += Mergesort(A,mid+1,high)
        count += Merge(A,low,mid,high)
    
    return count

A = [1,20,6,4,5]
print(Mergesort(A,0,4))
