class Solution(object):
    def evenNumberBitwiseORs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                l.append(nums[i])
        s=0
        for i in l:
            s=s|i
        return s


        