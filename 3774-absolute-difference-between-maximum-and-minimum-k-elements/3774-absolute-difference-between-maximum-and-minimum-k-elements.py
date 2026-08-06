class Solution(object):
    def absDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s1=0
        s=0
        t=sorted(nums)
        for i in range(k):
            s+=t[i]
            s1+=t[-(i+1)]
        return abs(s1-s)