class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        p=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                if l<=len(nums[i:j])<=r:
                    p.append(nums[i:j])
        s=0
        k=[]
        m=[]
        for i in range(len(p)):
            s=sum(p[i])
            k.append(s)
            if k[i]>0:
                m.append(k[i])
        if len(m)==0:
            return -1
        return min(m)
        
                
            
