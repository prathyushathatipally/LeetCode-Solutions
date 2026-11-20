class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l=[[]]
        for i in range(len(nums)):
            k=[]
            for j in range(len(l)):
                k.append(l[j]+[nums[i]])
            l=l+k
        return l
        