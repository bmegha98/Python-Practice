'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
'''

class Solution(object):
    def determineMedian(self,k,A,size):
        if size % 2 == 0 :
            return (A[k-1]+ A[k-2]) / float(2)
        else:
            return A[k-1]
        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        
        m , n = len(nums1),len(nums2)
    
        num = [0]*(m+n)
        i ,j,k = 0 ,0,0

        while i<m and j<n:
            if nums1[i] <= nums2[j]:
                num[k] = nums1[i]
                i += 1
            else:
                num[k] = nums2[j]
                j += 1
            k += 1
            if k == (m + n)//2+1:
                med = self.determineMedian(k,num,m + n)
                return med
            
        
        while i<m:
            num[k] = nums1[i]
            i += 1
            k += 1
            if k == (m + n)//2+1:
                med = self.determineMedian(k,num,m + n)
                return med
        
        while j<n:
            num[k] = nums2[j]
            j += 1
            k += 1
            if k == (m + n)//2+1:
                med = self.determineMedian(k,num,m + n)
                return med
