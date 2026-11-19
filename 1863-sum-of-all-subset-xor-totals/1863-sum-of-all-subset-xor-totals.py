class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[[]]
        for i in range(len(nums)):
            k=[]
            for j in range(len(l)):
                k.append(l[j]+[nums[i]])
            l=l+k
        l.remove([])
        s=0
        for i in range(len(l)):
            x=0
            for j in range(len(l[i])):
                x=x^l[i][j]
            s=s+x
        return s
          