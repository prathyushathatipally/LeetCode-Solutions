class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        start=min(nums)
        end=max(nums)
        l=[]
        for i in range(start,end+1):
            if i not in nums:
                l.append(i)
        return l
        