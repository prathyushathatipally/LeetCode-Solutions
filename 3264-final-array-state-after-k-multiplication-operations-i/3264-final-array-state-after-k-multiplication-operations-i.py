class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        s=0
        for i in range(k):
            l=[]
            t=sorted(nums)
            s=t[0]*multiplier
            l.append(s)
            index=nums.index(t[0])
            nums[index]=s
        return nums
        