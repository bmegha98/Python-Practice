'''
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
'''

class Solution(object):
    def Temporary(self,res,cur_res,candidates,remaining):
        if remaining == 0 :
            res.append(cur_res[:])
            return
        for cand in candidates:
            if cand <= remaining and (not cur_res or cur_res[-1] >= cand):
                cur_res.append(cand)
                self.Temporary(res,cur_res,candidates,remaining-cand)
                cur_res.pop()
        return
                
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort(reverse = True)
        res = []
        cur_res = []
        self.Temporary(res,cur_res,candidates,target)
        return res
        
