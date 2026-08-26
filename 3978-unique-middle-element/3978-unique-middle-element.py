class Solution(object):
    def isMiddleElementUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        k=nums[n//2]
        if nums.count(k)==1:
            return True
        return False




        