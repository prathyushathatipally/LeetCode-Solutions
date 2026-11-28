class Solution(object):
    def minMergedInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=[]
        l=[]
        for i in range(0,len(nums),2):
            temp=str(nums[i])+str(nums[i+1])
            l.append(int(temp))
        return min(l)