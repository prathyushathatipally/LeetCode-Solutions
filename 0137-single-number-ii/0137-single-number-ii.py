class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in range(len(nums)):
            if nums.count(nums[i])==1:
                l.append(nums[i])
        return int("".join(map(str,l)))
        