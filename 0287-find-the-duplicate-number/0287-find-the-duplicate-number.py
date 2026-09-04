class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=set()
        l1=set()
        for i in range(len(nums)):
            if nums[i] not in l:
                l.add(nums[i])
            else:
                l1.add(nums[i])
        return int("".join(map(str,l1)))
        