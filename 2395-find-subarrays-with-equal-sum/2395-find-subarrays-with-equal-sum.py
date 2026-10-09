class Solution(object):
    def findSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                if len(nums[i:j])==2:
                    l.append(nums[i:j])
        s=0
        k=[]
        for i in range(len(l)):
            s=sum(l[i])
            if s in k:
                return True
            k.append(s)
        return False
            
        