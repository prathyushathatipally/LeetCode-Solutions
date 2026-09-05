class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=[]
        l1=[]
        for i in range(len(nums)):
            if nums[i]>0:
                l.append(nums[i])
            else:
                l1.append(nums[i])
        k=[]
        for i in range(len(l)):
            k.append(l[i])
            k.append(l1[i])
        return k