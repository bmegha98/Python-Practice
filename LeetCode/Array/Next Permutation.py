'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        first , second = -1 , -1
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                first = i-1
                break
        if first == -1:
            nums[:] = sorted(nums[:])
        else:
            for j in range(len(nums)-1,0,-1):
                if nums[j] > nums[first]:
                    second = j
                    break
            temp = nums[first]
            nums[first] = nums[second]
            nums[second] = temp
            nums[first+1 :] = sorted(nums[first+1:])
            
        
