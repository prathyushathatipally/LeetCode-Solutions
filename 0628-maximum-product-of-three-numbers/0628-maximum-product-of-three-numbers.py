class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # current_min=nums[0]
        # current_max=nums[0]
        # maximum=nums[0]
        # for i in range(1,len(nums)):
        #     if nums[i]<0:
        #         current_max,current_min=current_min,current_max
        #     current_max=max(nums[i],current_max*nums[i])
        #     current_min=min(nums[i], current_min*nums[i])
        #     maximum=max(current_max,maximum)
        # return maximum
        nums=sorted(nums)

        k=nums[-1]*nums[-2]*nums[-3]
        s=nums[0]*nums[1]*nums[-1]
        return max(k,s)