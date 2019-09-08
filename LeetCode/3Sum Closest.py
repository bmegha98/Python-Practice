'''
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum
of the three integers.You may assume that each input would have exactly one solution.
'''

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 3 : return sum(nums)
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:continue
            start = i+1
            end = len(nums) - 1
            while start < end:
                s = nums[i] + nums[start] + nums[end]
                ans = abs(target - s)
                if res == [] or ans < res[0]:
                    res = [ans,s]
                if s == target:return s
                elif s < target : start += 1
                else : end -= 1
        
        return res[1]
        
