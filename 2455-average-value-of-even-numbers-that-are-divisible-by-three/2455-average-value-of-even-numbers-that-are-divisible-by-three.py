class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l=[]
        for i in range(len(nums)):
            if nums[i]%2==0:
                l.append(nums[i])
        m=[]
        for i in range(len(l)):
            if l[i]%3==0:
                m.append(l[i])
        if len(m)==0:
            return 0
        total=sum(m)
        avg=total/len(m)
        return avg



