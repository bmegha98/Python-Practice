'''
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that 
the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container
contains the most water.

Note: You may not slant the container and n is at least 2.
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        first = 0
        last = len(height) - 1
        area = 0
        while first < last :
            A = min(height[first],height[last]) * (last - first)
            if area < A :
                area = A
            if height[first] < height[last]:
                first += 1
            else:
                last -= 1
        return area
