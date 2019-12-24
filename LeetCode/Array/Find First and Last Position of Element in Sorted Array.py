'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].
'''
'''
# Using another approach:
def First(A,l,h,key):
    while l<=h :
        m = (l+h)//2
        if A[m] == key and (m == 0 or A[m-1] < key):return m
        elif A[m] < key : l = m + 1
        else : h = m - 1
    return -1

def Last (A, l , h , key):
    while l<=h :
        m = (l+h)//2
        if A[m] == key and (m == len(A)-1 or A[m+1] > key):return m
        elif A[m] <= key : l = m + 1
        else : h = m - 1
    return -1

'''
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums: return [-1,-1]
        if len(nums) == 1:
            if nums[0] == target: return [0,0]
            return [-1,-1]
        
        l , h = 0, len(nums)-1
        
        while l<=h:
            m = (l+h)//2
            if nums[m] == target :
                start , end = m , m
                while start >= 1 and nums[start] == nums[start-1]:
                    start -= 1
                while end < len(nums)-1 and nums[end] == nums[end+1]:
                    end += 1
            
                return [start,end]
        
            elif nums[m] < target :
                l = m+1
            else: h = m-1
        return [-1,-1]
