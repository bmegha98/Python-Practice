'''
Given an array A of integers. The task is to complete the function which returns an integer denoting the length of the longest 
sub-sequence such that elements in the sub-sequence are consecutive integers,the consecutive numbers can be in any order.
'''
def findLongestConseqSubseq(arr, n):
    s=set()
    for ele in arr:s.add(ele)
    ans=0
    for i in range(n):
        if (arr[i]-1) not in s:
            j=arr[i]
            while j in s:
                j+=1
            ans=max(ans,j-arr[i])
    return ans
