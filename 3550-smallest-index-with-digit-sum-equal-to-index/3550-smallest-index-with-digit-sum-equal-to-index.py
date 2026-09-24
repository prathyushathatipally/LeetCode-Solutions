class Solution(object):
    def smallestIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in range(len(nums)):
            temp=nums[i]
            s=0
            while temp>0:
                digits=temp%10
                s+=digits
                temp=temp//10
            l.append(s)
        m=[]
        for i in range(len(l)):
            if l[i]==i:
                m.append(l[i])
        if len(m)==0:
            return -1
        return min(m)

        