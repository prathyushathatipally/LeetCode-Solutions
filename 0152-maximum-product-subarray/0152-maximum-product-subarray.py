class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_min=nums[0]
        current_max=nums[0]
        maximum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                current_min,current_max=current_max,current_min
            current_max=max(nums[i],nums[i]*current_max)
            current_min=min(nums[i],nums[i]*current_min)

            maximum=max(current_max,maximum)
        return maximum

        