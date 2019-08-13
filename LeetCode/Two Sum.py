'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
'''
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in nums[i+1:]:
                ind = nums[i+1:].index(rem)
                l = [i,i+ind+1]
                return l
                
