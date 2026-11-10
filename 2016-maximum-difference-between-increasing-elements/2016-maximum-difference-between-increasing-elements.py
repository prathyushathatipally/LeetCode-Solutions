class Solution(object):
    def maximumDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    k=nums[j]-nums[i]
                    l.append(k)
        maxi=0
        for i in range(len(l)):
            if l[i]>maxi:
                maxi=l[i]
        if len(l)==0:
            return -1
        return maxi

        
        