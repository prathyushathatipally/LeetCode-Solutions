class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s=0
        l=[]
        for i in range(len(nums)):
            l.append(bin(i)[2:])
        for i in range(len(l)):
            if l[i].count("1")==k:
                s=s+nums[i]
        return s


    



                    


        