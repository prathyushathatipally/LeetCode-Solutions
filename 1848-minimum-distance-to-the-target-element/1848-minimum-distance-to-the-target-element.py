class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        # l=[]
        # for i in range(len(nums)):
        #     if nums[i] not in l:
        #         l.append(nums[i])
        l=[]
        for i in range(len(nums)):
            if nums[i]==target:
                l.append(abs(i-start))
        return min(l)