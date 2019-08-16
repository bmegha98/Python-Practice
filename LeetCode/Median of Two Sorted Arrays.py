'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.
'''

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)
        if n % 2 == 0:
            first = nums1[n//2]
            second = nums1[n//2 - 1]
            res = (first+second)/2.0
            return res
        else :
            return nums1[int(n/2)]
