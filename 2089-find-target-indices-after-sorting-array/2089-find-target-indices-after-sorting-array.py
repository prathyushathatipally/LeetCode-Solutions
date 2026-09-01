class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=[]
        s=sorted(nums)
        for i in range(len(s)):
            if s[i]==target:
                l.append(i)
        return l
        