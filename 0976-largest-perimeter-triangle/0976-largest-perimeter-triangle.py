class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer=0
        nums=sorted(nums)
        for i in range(len(nums)-1,1,-1):
            a=nums[i-2]
            b=nums[i-1]
            c=nums[i]
            if a+b>c:
                answer=a+b+c
                break
        return answer






       
                

        