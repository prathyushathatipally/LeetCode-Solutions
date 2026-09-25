class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start=0
        end=len(nums)
        l=[]
        for i in range(start,end+1):
            l.append(i)
        m=[]
        for i in range(len(l)):
            if l[i] not in nums:
                m.append(l[i])
        return m[0]


        