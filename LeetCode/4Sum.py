'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find 
all unique quadruplets in the array which gives the sum of target.
Note:
The solution set must not contain duplicate quadruplets.
'''
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        res = []
        if len(nums) < 4 : return res
        if len(nums) == 4 : return [nums] if sum(nums) == target else []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:continue
            for j in range(i+1,len(nums)-2):
                start = j+1
                end = len(nums)-1
                while start < end:
                    temp = [nums[i],nums[j],nums[start],nums[end]]
                    t = sum(temp)
                    if t == target:
                        if temp not in res:
                            res.append(temp)
                        start += 1
                        end -= 1
                    elif t < target:
                        start += 1
                    else:
                        end -= 1
        return res
