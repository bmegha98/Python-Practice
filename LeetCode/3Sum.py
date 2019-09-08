'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.
'''
#TLE
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3 : return []
        if len(nums) == 3 : return [] if sum(nums) else [nums]
        nums.sort()
        res = []
        for i in range(len(nums)-2):
            
            if nums[i] > 0 : break
            start = i + 1
            end = len(nums) - 1
            
            if nums[i] + nums[start] + nums[start + 1] > 0 : break
                
            while start < end :
                l = [nums[i] , nums[start] , nums[end]]
                n = sum(l)
                if not n :
                    if l not in res :
                        res.append(l)
                    start += 1
                    end -= 1
                elif n > 0 : end -= 1
                else : start += 1
        
        return res
'''
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3 : return []
        if len(nums) == 3 : return [] if sum(nums) else [nums]
        nums.sort()
        res = []
        for i in range(len(nums)-1):
            #if i is searched again,skip it
            if i > 0 and nums[i] == nums[i-1]:continue
                
            if nums[i] > 0 : break
            s = set()
            j = i+1
            while j < len(nums):
                rem = -(nums[i] + nums[j])
                if rem in s :
                    res.append([nums[i],rem,nums[j]])
                    #to remove duplicates
                    while j < len(nums) - 1 and nums[j] == nums[j + 1]:
                        j = j + 1
                else:
                    s.add(nums[j])
                j += 1
        
        return res

