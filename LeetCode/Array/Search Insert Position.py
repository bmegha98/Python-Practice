'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were 
inserted in order.

You may assume no duplicates in the array.

'''
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l , h = 0 , len(nums)-1
        while l<=h:
            m = (l+h)//2
            if nums[m] == target: return m
            elif nums[m] < target : l = m+1
            else : h = m-1
        if l < len(nums) :
            if nums[l] > target: return l
            else: return l+1
        else:
            return l
        
