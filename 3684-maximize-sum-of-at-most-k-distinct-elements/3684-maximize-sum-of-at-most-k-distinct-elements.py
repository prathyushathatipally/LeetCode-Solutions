class Solution(object):
    def maxKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l=[]
        for i in range(len(nums)):
            if nums[i] not in l:
                l.append(nums[i])
        l=sorted(l,reverse=True)
        s=l[:k]
        return s




        