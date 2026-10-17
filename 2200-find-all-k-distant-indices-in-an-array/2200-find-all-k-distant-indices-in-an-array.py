class Solution(object):
    def findKDistantIndices(self, nums, key, k):
        """
        :type nums: List[int]
        :type key: int
        :type k: int
        :rtype: List[int]
        """
        l=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if abs(i-j)<=k and nums[j]==key:
                    l.append(i)
                    break
        return l

                   