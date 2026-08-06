class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                l.append(nums[i:j+1])
        s=0
        for i in range(len(l)):
            l1=[]
            for j in l[i]:
                if j not in l1:
                    l1.append(j)
            s+=len(l1)**2
        return s
        



                
        