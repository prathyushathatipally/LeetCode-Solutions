class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=0
        max_sum=nums[0]
        for i in range(len(nums)):
            s+=nums[i]
            if s>max_sum:
                max_sum=s
            if s<0:
                s=0
        return max_sum
        