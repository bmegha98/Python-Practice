'''
Given two sorted arrays A and B. The task is to complete the function max_path_sum that takes 4 argument, the first two arguments 
represent the 2 arrays A[] and B[] and the last two arguments l1, l2 denote the size of array A and B respectively. 
The function returns the sum of the maximum sum path to reach from beginning of any array to end of any of the two arrays .
'''
def maxSumPath(arr1, arr2, m, n):
    i,j,sum1,sum2,Sum=0,0,0,0,0
    while i<m and j<n:
        if arr1[i]<arr2[j]:
            sum1+=arr1[i]
            i+=1
        elif arr1[i]>arr2[j]:
            sum2+=arr2[j]
            j+=1
        else:
            Sum+=max(sum1,sum2)
            sum1=0
            sum2=0
            while i < m and j < n and arr1[i]==arr2[j]: 
                Sum += arr1[i] 
                i+=1
                j+=1
    while i < m: 
        sum1 += arr1[i] 
        i+=1
   
    while j < n: 
        sum2 += arr2[j] 
        j+=1
      
    
    Sum += max(sum1,sum2) 
      
    return Sum
                
