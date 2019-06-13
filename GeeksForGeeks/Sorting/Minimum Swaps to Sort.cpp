'''
Given an array of N distinct elementsA[ ]. The task is to find the minimum number of swaps required to sort the array. Your are required 
to complete the function which returns an integer denoting the minimum number of swaps, required to sort the array.
'''
'''
#TLE
def minSwaps(arr, n):
    count = 0
    for i in range(n-1):
        Min = i
        j = i+1
        while j<n:
            if arr[j]<arr[Min]:Min = j
            j+=1
        if Min!= i:
            arr[Min],arr[i] = arr[i],arr[Min]
            count+=1
    
    return count
        
'''
int minSwaps(int A[], int N){
    int count = 0;
    for(int i =0;i<N;i++)
    {
        int k = i,t;
        for(int j=i+1;j<N;j++)
        {
            if(A[j]<A[k])
            k = j;
        }
        if(k!=i)
        {
            t = A[i];
            A[i]=A[k];
            A[k]=t;
            count++;
        }
    }
    return count;
}
