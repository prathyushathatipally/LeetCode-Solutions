class Solution(object):
    def minimumAverage(self, nums):
        """
        :type nums: List[int]
        :rtype: float
        """
        nums=sorted(nums)
        l1=[]
        i=0
        j=len(nums)-1
        while i<j:
            k=nums[i]+nums[j]
            avg=k/2.0
            l1.append(avg)
            i+=1
            j-=1
        return min(l1)
        