class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=0
        m=max(nums)
        for i in range(len(nums)):
            c=c+m-nums[i]
        return c
